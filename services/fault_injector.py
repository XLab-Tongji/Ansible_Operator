# -*- coding: utf-8 -*

import sys
from utils.ansible_runner import Runner
sys.path.append('../')


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
