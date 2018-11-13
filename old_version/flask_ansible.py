from flask import Flask
from flask_restful import Resource, Api

import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C

app = Flask(__name__)
api = Api(app)


class ResultCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin
    """

    def v2_runner_on_ok(self, result, **kwargs):
        """Print a json representation of the result

        This method could store the result in an instance attribute for retrieval later
        """
        host = result._host
        self.result = result._result
        print(json.dumps({host.name: result._result}, indent=4))


def exec_ansible(module, args, host):
    Options = namedtuple('Options',
                         ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check',
                          'diff'])
    # initialize needed objects
    loader = DataLoader()
    options = Options(connection='ssh', module_path=['~/anaconda3/envs/Flask/lib/python2.7/site-packages/ansible/modules/'],
                      forks=100, become=None, become_method=None, become_user=None, check=False,
                      diff=False)
    passwords = dict(vault_pass='secret')

    # Instantiate our ResultCallback for handling results as they come in


    # create inventory and pass to var manager
    # use path to host config file as source or hosts in a comma separated string
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    results_callback = ResultCallback()

    # create play with tasks
    play_source = dict(
        hosts=host,
        tasks=[
            dict(action=dict(module=module, args=args), register='output'),
            dict(action=dict(module='debug', args=dict(msg='{{output.stdout}}')))
        ]
    )
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    # actually run it
    tqm = None
    try:
        tqm = TaskQueueManager(
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            options=options,
            passwords=passwords,
            stdout_callback=results_callback,  # Use our custom callback instead of the ``default`` callback plugin
        )
        result = tqm.run(play)
    finally:
        if tqm is not None:
            tqm.cleanup()

            # Remove ansible tmpdir
        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
    return results_callback.result


class HelloWorld(Resource):
    def get(self):
        return exec_ansible(module='shell', args='ls', host='Lab409-master')


class Load(Resource):
    def get(self):
        createuser_command="docker exec -d $(docker ps |grep clearwater-cassandra |awk {'print $1'}) bash -c \"date > /var/log/zqb_log1.txt&&/usr/share/clearwater/crest-prov/src/metaswitch/crest/tools/stress_provision.sh 1000 >> /var/log/zqb_log1.txt\"&& sleep 10s&& docker cp 57d75:/var/log/zqb_log1.txt /var/log/zqb_log1.txt&& cat /var/log/zqb_log1.txt"
        createuser_result=exec_ansible(module='shell', args=createuser_command, host='cassandra')['msg']
        workload_command="docker exec -d $(docker ps |grep rainlf/clearwater-stress-ng |awk {'print $1'}) bash -c \"date > /var/log/zqb_log2.txt&&/usr/share/clearwater/bin/run_stress default.svc.cluster.local 500 10 --initial-reg-rate 100 --multiplier 450 >> /var/log/zqb_log2.txt\"&& sleep 10s&& docker cp 58c95964392f:/var/log/zqb_log2.txt /var/log/zqb_log2.txt&& cat /var/log/zqb_log2.txt"
        workload_result=exec_ansible(module='shell', args=workload_command, host='stress-ng')['msg']
        return {'createuser': createuser_result,'workload': workload_result}

class GetSVC(Resource):
    def get(self):
        return exec_ansible(module='k8s_facts', args='api_version=v1 kind=Service namespace=sock-shop', host='Lab409-master')


class Zabbix(Resource):
    def get(self):
        command=['apt-get install zabbix-agent -y',
                 'sed -i "s/Server=127.0.0.1/Server=192.168.1.20/g" /etc/zabbix/zabbix_agentd.conf',
                 'sed -i "s/ServerActive=127.0.0.1/ServerActive=192.168.1.20/g" /etc/zabbix/zabbix_agentd.conf',
                 'sed -i "s/Hostname=Zabbix server/Hostname=ubuntu23/g" /etc/zabbix/zabbix_agentd.conf',
                 'service zabbix-agent restart']
        result=[]
        for i in range(0,len(command)):
            r=exec_ansible(module='shell', args=command[i], host='cw')
            if r.has_key('msg'):
                result.append(r['msg'])
            else:
                result.append('')
    
        return {'apt-get install zabbix-agent -y':result[0],
                'sed -i "s/Server=127.0.0.1/Server=192.168.1.20/g" /etc/zabbix/zabbix_agentd.conf':result[1],
                'sed -i "s/ServerActive=127.0.0.1/ServerActive=192.168.1.20/g" /etc/zabbix/zabbix_agentd.conf':result[2],
                'sed -i "s/Hostname=Zabbix server/Hostname=ubuntu23/g" /etc/zabbix/zabbix_agentd.conf':result[3],
                'service zabbix-agent restart':result[4]}


api.add_resource(HelloWorld, '/')
api.add_resource(Load, '/load')
api.add_resource(Zabbix, '/zabbix')
api.add_resource(GetSVC, '/svc')

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 8081,debug = True )
