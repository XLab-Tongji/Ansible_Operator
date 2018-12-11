# -*- coding: utf-8 -*

class Config(object):
    def __init__(self):
        pass

    remote_user = 'root'
    module_path = ['~/anaconda3/envs/Flask/lib/python2.7/site-packages/ansible/modules/']
    user_name = 'lab'
    password = '409'

    # prometheus config

    PROMETHEUS_URL = 'http://10.60.38.181:13002'
    PROMETHEUS_URL2 = 'http://10.60.38.181:13001'
    CONTAINERLIST = ['docker-compose_carts-db_1', 'docker-compose_carts_1', 'docker-compose_catalogue-db_1',
                     'docker-compose_catalogue_1', 'docker-compose_edge-router_1', 'docker-compose_front-end_1',
                     'docker-compose_kibana_1',
                     'docker-compose_orders-db_1', 'docker-compose_orders_1', 'docker-compose_payment_1',
                     'docker-compose_queue-master_1',
                     'docker-compose_rabbitmq_1', 'docker-compose_shipping_1', 'docker-compose_user-db_1',
                     'docker-compose_user_1']
    INSTANCELIST = ['carts:80', 'catalogue:80', 'edge-router:80', 'orders:80', 'payment:80', 'shipping:80', 'user:80']
    QUERY_API = '/api/v1/query'
    RANGE_QUERY_API = '/api/v1/query_range'
    RESOLUTION = '10'  # default: 10s
    OUTPUTFILE = 'result.csv'  # default: result.csv
    PERIOD = 1440  # unit: miniute, default 60, Resolution=10s

    TiandiMetricNames = [
        'container_fs_io_current',
        'container_fs_usage_bytes',
        'container_fs_reads_bytes_total',
        'container_fs_writes_bytes_total',
        'memory_usage',
        'network_receive_bytes',
        'network_transmit_bytes',
        'cpu_usage_percent',
        'memory_cache_usage_bytes'
    ]

    # 2针对url2
    TiandiMetricNames2 = [
        'request_duration_seconds_count',
        'request_duration_seconds_bucket'
    ]

    TiandiQueryList = [
        'container_fs_io_current{name="%s"}',
        'container_fs_usage_bytes{name="%s"}',
        'sum by (name) (rate(container_fs_reads_bytes_total{name="%s"}[1m]))',
        'sum by (name) (rate(container_fs_writes_bytes_total{name="%s"}[1m]))',
        'container_memory_usage_bytes{name = "%s"}',
        'sum by (name) (rate(container_network_receive_bytes_total{name="%s",container_label_org_label_schema_group=""}[1m]))',
        'sum by (name) (rate(container_network_transmit_bytes_total{name="%s",container_label_org_label_schema_group=""}[1m]))',
        'sum by (name) (rate(container_cpu_usage_seconds_total{image!="",name="%s",container_label_org_label_schema_group=""}[1m]))',
        # 1m指1分钟
        'container_memory_cache{name="%s",container_label_org_label_schema_group=""}',
    ]

    TiandiQueryList2 = [
        'sum by (instance) (rate(request_duration_seconds_count{instance="%s"}[1m]))',
        'sum by (instance) (rate(request_duration_seconds_bucket{instance="%s"}[1m]))'
    ]

