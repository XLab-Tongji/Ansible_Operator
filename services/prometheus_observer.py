# -*- coding: utf-8 -*

import requests
import time
import logging
import datetime

from view_model.prometheus_repository import PrometheusRepository
from utils.config import Config


class PrometheusObserver(object):
    def __init__(self):
        pass

    @staticmethod
    def build_entity_metrics(queryConfig):
        entityMetrics = []
        #conbine entityNames and entityMetrics
        type = queryConfig['entity_type']
        for entity in queryConfig['entity_list']:
            for metric in queryConfig['metric_list']:
                entityMetrics.append(type+'/'+entity+"/"+metric)
        return entityMetrics

    @staticmethod
    def query_entity_metric_values(metricnames, querylist, prometheusConfig, resolution, end_time, start_time):
        csvset = dict()
        for index in range(len(metricnames)):
            list = metricnames[index].split('/')
            query = querylist[index % len(querylist)] % list[1]
            response = requests.get(prometheusConfig['url'] + prometheusConfig['query_api'],
                                    params={
                                        'query': query, 'start': start_time,
                                        'end': end_time, 'step': resolution},
                                    auth=(prometheusConfig['auth_user'], prometheusConfig['auth_password']))

            results = response.json()['data']['result']
            if results != []:
                for value in results[0]['values']:
                    if index == 0:
                        csvset[value[0]] = [value[1]]
                    else:
                        if value[0] in csvset:
                            csvset[value[0]].append(value[1])
                        else:
                            # print(results)
                            csvset[value[0]] = []
                            for count in range(index):
                                csvset[value[0]].append('null');
                            csvset[value[0]].append(value[1])
                for timestamp in csvset.keys():
                    if len(csvset[timestamp]) <= index:
                        csvset[timestamp].append("null")
            else:
                for timestamp in csvset.keys():
                    csvset[timestamp].append("null")
            # 按竖列输出的数据！！！null代表没有该项数据
        return csvset

    @staticmethod
    def run(dto):
        # 处理开始时间和结束时间
        if Config.PERIOD != '':
            end_time = int(time.time())
            start_time = end_time - 60 * Config.PERIOD
        else:
            end_time = datetime.datetime.fromtimestamp(dto['from'])
            start_time = datetime.datetime.fromtimestamp(dto['to'])

        metricnames1 = PrometheusObserver.build_entity_metrics(Config.QUERY_CONFIG1)
        csvset1 = PrometheusObserver.query_entity_metric_values(
            metricnames=metricnames1,
            querylist=Config.QUERY_CONFIG1['query_list'],
            prometheusConfig=Config.PROMETHEUS_CONFIG1,
            resolution=Config.PROMETHEUS_RESOLUTION,
            start_time=start_time,
            end_time=end_time
        )

        metricnames2 = PrometheusObserver.build_entity_metrics(Config.QUERY_CONFIG2)
        csvset2 = PrometheusObserver.query_entity_metric_values(
            metricnames=metricnames2,
            querylist=Config.QUERY_CONFIG2['query_list'],
            prometheusConfig=Config.PROMETHEUS_CONFIG2,
            resolution=Config.PROMETHEUS_RESOLUTION,
            start_time=start_time,
            end_time=end_time
        )

        datasetHeader = []
        datasetHeader += metricnames1
        datasetHeader += metricnames2

        # 生成数据集
        logging.info("Querying metric values succeeded, rows of data: %s", len(csvset1))
        return PrometheusRepository.create_prometheus_stream_view_model(datasetHeader, csvset1, csvset2)
