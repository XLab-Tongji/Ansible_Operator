# -*- coding: utf-8 -*

import sys
import random
from utils.ansible_runner import Runner

sys.path.append('../')

Hosts=["192.168.199.31",
"192.168.199.32",
"192.168.199.33",
"192.168.199.34",
"192.168.199.35"
]
HostsVM=["192.168.199.21",
"192.168.199.22",
"192.168.199.23",
"192.168.199.24",
"192.168.199.25"
]
Cmd=["blade create cpu fullload",
"blade create network delay --interface ens160",
"blade create disk fill --size 1000"
]

class FaultInjector(object):
    def __init__(self):
        pass

    @staticmethod
    def inject_cpu(dto):
        r = Runner()
        r.run_ad_hoc(
            hosts=dto['host'],
            module='shell',
            args='stress -c 1 -t ' + dto['inject_duration'] + ' > /dev/null 2>&1'
        )
        result = r.get_adhoc_result()
        return result

    @staticmethod
    def inject_mem(dto):
        r = Runner()
        r.run_ad_hoc(
            hosts=dto['host'],
            module='shell',
            args='stress --vm 4 --vm-bytes 1G --vm-hang ' + dto['inject_duration'] + ' -t '
                 + dto['inject_duration'] + ' > /dev/null 2>&1'
        )
        result = r.get_adhoc_result()
        return result

    @staticmethod
    def inject_io(dto):
        r = Runner()
        r.run_ad_hoc(
            hosts=dto['host'],
            module='shell',
            args='stress -i 100 -t ' + dto['inject_duration'] + ' > /dev/null 2>&1'
        )
        result = r.get_adhoc_result()
        return result

    #metal
    @staticmethod
    def chaosinject(dto):
        i=random.randint(0, 4)
        j=random.randint(0, 2)
        r = Runner()
        r.run_ad_hoc(
            hosts=Hosts[i],
            module='shell',
            args=Cmd[j]+" --timeout " + dto['inject_duration']
        )
        result = r.get_adhoc_result()
        return result
    #test
    @staticmethod
    def chaosinject1(dto):
        #i=random.randint(0, 4)
        #j=random.randint(0, 2)
        r = Runner()
        r.run_ad_hoc(
            hosts="192.168.199.31",
            module='shell',
            args="blade create disk fill --size 1000 --timeout " + dto['inject_duration']
        )
        result = r.get_adhoc_result()
        return result
    #vm
    @staticmethod
    def chaosinjectvm(dto):
        i=random.randint(0, 4)
        j=random.randint(0, 2)
        r = Runner()
        r.run_ad_hoc(
            hosts=HostsVM[i],
            module='shell',
            args=Cmd[j]+" --timeout " + dto['inject_duration']
        )
        result = r.get_adhoc_result()
        return result
