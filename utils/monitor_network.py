#!/usr/bin/python
# coding=utf8

import os
import time
from datetime import datetime

import psutil
from sql_process import DbConn


# 处理网络流量
class NetworkTraffic(object):
    network_keys = []

    old_sent, old_receive = {}, {}
    new_sent, new_receive = {}, {}

    def __init__(self):
        pass

    # 获取网络发包和收包
    def get_network_counters(self):
        sent = {}
        receive = {}
        network_counters = psutil.net_io_counters(pernic=True)
        self.network_keys = network_counters.keys()

        for key in self.network_keys:
            sent[key] = network_counters.get(key).bytes_sent
            receive[key] = network_counters.get(key).bytes_recv
        return sent, receive

    # 处理统计5分钟内的网络流量
    def handle_network_counters(self):

        network_times = {}
        net_input, net_output = {}, {}

        self.old_sent, self.old_receive = self.get_network_counters()
        network_times['old'] = datetime.strftime(datetime.now(), ('%Y-%m-%d %H:%M:%S'))

        time.sleep(60)
        self.new_sent, self.new_receive = self.get_network_counters()
        network_times['new'] = datetime.strftime(datetime.now(), ('%Y-%m-%d %H:%M:%S'))

        for key in self.network_keys:
            net_output[key] = (self.new_sent[key] - self.old_sent[key]) / 1024
            net_input[key] = (self.new_receive[key] - self.old_receive[key]) / 1024

        return net_output, net_input, network_times


def run():
    monitor_hostname = os.popen('hostname').read().splitlines()[0]

    monitor_network = NetworkTraffic()

    net_out, net_in, network_time = monitor_network.handle_network_counters()

    db = DbConn('monitor_network')
    for key in net_out.keys():
        db.insert(
            minion_id=monitor_hostname,
            network_key=key,
            network_in=net_in[key],
            network_out=net_out[key],
            network_time=network_time['old']
        )
    db.close()


if __name__ == '__main__':
    run()
