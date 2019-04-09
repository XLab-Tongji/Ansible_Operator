# -*- coding: utf-8 -*


class K8sRepository(object):
    def __init__(self):
        pass

    @staticmethod
    def create_k8s_namespace_view_model(result):
        success = []

        try:
            for each_host in result['success']:
                for each_resource in result['success'][each_host.encode('raw_unicode_escape')]['resources']:
                    temp = dict()
                    temp['creationTimestamp'] = each_resource['metadata']['creationTimestamp']
                    temp['name'] = each_resource['metadata']['name']
                    temp['uid'] = each_resource['metadata']['uid']
                    success.append(temp)
        except:
            success = {}

        result['detail'] = result['success']
        result['success'] = success
        return result

    @staticmethod
    def create_k8s_node_view_model(result):
        success = []

        try:
            for each_host in result['success']:
                for each_resource in result['success'][each_host.encode('raw_unicode_escape')]['resources']:
                    temp = dict()
                    temp['creationTimestamp'] = each_resource['metadata']['creationTimestamp']
                    temp['labels'] = each_resource['metadata']['labels']['kubernetes.io/role']
                    temp['name'] = each_resource['metadata']['name']
                    temp['uid'] = each_resource['metadata']['uid']
                    success.append(temp)
        except:
            success = {}

        result['detail'] = result['success']
        result['success'] = success
        return result

    @staticmethod
    def create_k8s_svc_view_model(result):
        success = []

        try:
            for each_host in result['success']:
                for each_resource in result['success'][each_host.encode('raw_unicode_escape')]['resources']:
                    temp = dict()
                    temp['creationTimestamp'] = each_resource['metadata']['creationTimestamp']
                    temp['labels'] = each_resource['metadata']['labels']
                    temp['name'] = each_resource['metadata']['name']
                    temp['namespace'] = each_resource['metadata']['namespace']
                    temp['clusterIP'] = each_resource['spec']['clusterIP']
                    success.append(temp)
        except:
            success = {}

        result['detail'] = result['success']
        result['success'] = success
        return result

    @staticmethod
    def create_k8s_deployment_view_model(result):
        success = []

        try:
            for each_host in result['success']:
                for each_resource in result['success'][each_host.encode('raw_unicode_escape')]['resources']:
                    temp = dict()
                    temp['creationTimestamp'] = each_resource['metadata']['creationTimestamp']
                    temp['labels'] = each_resource['metadata']['labels']
                    temp['name'] = each_resource['metadata']['name']
                    temp['namespace'] = each_resource['metadata']['namespace']
                    temp['container_spec'] = each_resource['spec']['template']['spec']['containers']
                    success.append(temp)
        except:
            success = {}

        result['detail'] = result['success']
        result['success'] = success
        return result

    @staticmethod
    def create_k8s_pods_view_model(result):
        success = []

        try:
            for each_host in result['success']:
                for each_resource in result['success'][each_host.encode('raw_unicode_escape')]['resources']:
                    temp = dict()
                    temp['creationTimestamp'] = each_resource['metadata']['creationTimestamp']
                    temp['labels'] = each_resource['metadata']['labels']
                    temp['name'] = each_resource['metadata']['name']
                    temp['namespace'] = each_resource['metadata']['namespace']
                    temp['nodeName'] = each_resource['spec']['nodeName']
                    temp['hostIP'] = each_resource['status']['hostIP']
                    temp['podIP'] = each_resource['status']['podIP']
                    success.append(temp)
        except:
            success = {}

        result['detail'] = result['success']
        result['success'] = success
        return result