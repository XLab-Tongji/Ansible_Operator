# -*- coding: utf-8 -*
from utils.config import Config


class PrometheusRepository(object):
    def __init__(self):
        pass

    @staticmethod
    def create_prometheus_stream_view_model(metricnames, dataset1, dataset2):
        data_title = ['timestamp'] + metricnames
        data_body = []
        times = Config.PERIOD * 60 / int(Config.PROMETHEUS_RESOLUTION)
        num = 0
        for timestamp in sorted(dataset1.keys(), reverse=True):
            num = num + 1
            if (num > times): break
            if timestamp in dataset2:
                data_body.append([timestamp] + dataset1[timestamp]+dataset2[timestamp])

        return {'data_title': data_title, 'data_body': data_body}