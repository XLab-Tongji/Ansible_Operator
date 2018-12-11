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
    def query_tiandi_metric_names():
        metricName = []
        # 将container名字和列名结合
        for containerName in range(len(Config.CONTAINERLIST)):
            for index in range(len(Config.TiandiMetricNames)):
                metricName.append(Config.CONTAINERLIST[containerName] + "/" + Config.TiandiMetricNames[index])
        for instanceName in range(len(Config.INSTANCELIST)):
            for index in range(len(Config.TiandiMetricNames2)):
                metricName.append(Config.INSTANCELIST[instanceName] + "/" + Config.TiandiMetricNames2[index])
        return metricName

    @staticmethod
    def query_tiandi_metric1_names():
        metricName = []
        # 将container名字和列名结合
        for containerName in range(len(Config.CONTAINERLIST)):
            for index in range(len(Config.TiandiMetricNames)):
                metricName.append(Config.CONTAINERLIST[containerName] + "/" + Config.TiandiMetricNames[index])
        return metricName

    @staticmethod
    def query_tiandi_metric2_names():
        metricName = []
        # 将container名字和列名结合
        for instanceName in range(len(Config.INSTANCELIST)):
            for index in range(len(Config.TiandiMetricNames2)):
                metricName.append(Config.INSTANCELIST[instanceName] + "/" + Config.TiandiMetricNames2[index])
        return metricName

    @staticmethod
    def query_tiandi_metric_values1(metricnames, end_time, start_time):
        csvset = dict()
        for index in range(len(metricnames)):
            list = metricnames[index].split('/')
            response = requests.get(Config.PROMETHEUS_URL + Config.RANGE_QUERY_API,
                                    params={
                                        'query': Config.TiandiQueryList[index % len(Config.TiandiQueryList)] % list[0],
                                        'start': start_time,
                                        'end': end_time, 'step': Config.RESOLUTION}, auth=('admin', 'admin'))

            results = response.json()['data']['result']
            if results != []:
                for value in results[0]['values']:
                    if index == 0:
                        csvset[value[0]] = [value[1]]
                    else:
                        csvset[value[0]].append(value[1])
            else:
                for index in range(end_time, start_time, -10):
                    csvset[index].append("null")
            # 按竖列输出的数据！！！null代表没有该项数据
        return csvset

    @staticmethod
    def query_tiandi_metric_values2(metricnames, end_time, start_time):
        csvset = dict()
        for index in range(len(metricnames)):
            list = metricnames[index].split('/')
            query = Config.TiandiQueryList2[index % len(Config.TiandiQueryList2)] % list[0]
            response = requests.get(Config.PROMETHEUS_URL2 + Config.RANGE_QUERY_API,
                                    params={
                                        'query': Config.TiandiQueryList2[index % len(Config.TiandiQueryList2)] % list[
                                            0], 'start': start_time,
                                        'end': end_time, 'step': Config.RESOLUTION}, auth=('admin', 'admin'))

            results = response.json()['data']['result']
            if results != []:
                for value in results[0]['values']:
                    if index == 0:
                        csvset[value[0]] = [value[1]]
                    else:
                        csvset[value[0]].append(value[1])
            else:
                for index in range(end_time, start_time, -10):
                    csvset[index].append("null")
            # 按竖列输出的数据！！！null代表没有该项数据
        return csvset

    @staticmethod
    def run(dto):
        # 处理参数
        # metricnames = query_metric_names()
        metricnames = PrometheusObserver.query_tiandi_metric_names()
        # 处理抬头
        logging.info("Querying metric names succeeded, metric number: %s", len(metricnames))
        # csvset = query_metric_values(metricnames=metricnames)
        metricnames1 = PrometheusObserver.query_tiandi_metric1_names()
        metricnames2 = PrometheusObserver.query_tiandi_metric2_names()

        # 处理开始时间和结束时间
        if Config.PERIOD != '':
            end_time = int(time.time())
            start_time = end_time - 60 * Config.PERIOD
        else:
            end_time = datetime.datetime.fromtimestamp(dto['from'])
            start_time = datetime.datetime.fromtimestamp(dto['to'])

        csvset1 = PrometheusObserver.query_tiandi_metric_values1(metricnames=metricnames1, end_time=end_time, start_time=start_time)
        csvset2 = PrometheusObserver.query_tiandi_metric_values2(metricnames=metricnames2, end_time=end_time, start_time=start_time)
        # 生成数据集
        logging.info("Querying metric values succeeded, rows of data: %s", len(csvset1))
        return PrometheusRepository.create_prometheus_stream_view_model(metricnames, csvset1, csvset2)
