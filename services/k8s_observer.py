# -*- coding: utf-8 -*

import sys
import os
sys.path.append('../')
from utils.ansible_runner import Runner


class K8sObserver(object):
    def __init__(self):
        pass

    @staticmethod
    def fetch_playbook_path(name):
        APP_ROOT = os.getcwd()
        return os.path.join(APP_ROOT, 'static', 'playbook', name)

    @staticmethod
    def get_svc():
        r = Runner()
        r.run_playbook([K8sObserver.fetch_playbook_path('get_svc.yaml')])
        return r.get_playbook_result()

    @staticmethod
    def get_pods():
        r = Runner()
        r.run_playbook([K8sObserver.fetch_playbook_path('get_pod.yaml')])
        return r.get_playbook_result()
