#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This file is for pressure testing. Most of the time, it's useless to you.
'''

import os
import subprocess as subproc
import argparse
import json

GO_PATH = os.getenv('GOPATH', "~/Code/go")
SERVER_BIN = 'demo-server'
SERVER_IP = "127.0.0.1"
# PORT = 8080
SERVER_APPNAME = "demo-server"
SERVER_PROCTYPE = "web"
SERVER_PROCNAME = "echo-and-hello"

LAIN_DOMAIN = "lain.local"
CALICO_IP = "AUTO"
CALICO_PROFILE = "7d5af3a49034fe9de2b330a432b85e48"

ETCD_LAIN_APPS = "/lain/deployd/core_info"
LAINLET_WEBSERVICE = "http://localhost:9001"

def etcd_lain_apps_path(app_name, proc_type, proc_name):
    if proc_type == "":
        return ETCD_LAIN_APPS + "/" + app_name
    else:
        return "{}/{}/{}.{}.{}".format(ETCD_LAIN_APPS, app_name, app_name,
                proc_type, proc_name)

def set_etcd(port, amount):
    podInfos = []

    for i in range(amount):
        containerInfos = [{
                "Command": ["/server"],
                "ContainerId": str(id(port+i)),
                "ContainerIp": SERVER_IP,
                "Env": [
                    "LAIN_APPNAME={}".format(SERVER_APPNAME),
                    "LAIN_PROCNAME={}".format(SERVER_PROCNAME),
                    "LAIN_DOMAIN={}".format(LAIN_DOMAIN),
                    "CALICO_IP={}".format(CALICO_IP),
                    "CALICO_PROFILE={}".format(CALICO_PROFILE),
                    ],
                "Expose": port+i,
                "HostInterfaceName": "calicba3eeac301",
                "NodeIp": "192.168.77.21",
                "NodeName": "node1",
                "Volumes": []
                }]
        podInfo = {
                "Annotation": '{"mountpoint": []}',
                "ContainerInfos": containerInfos,
                "Dependencies":[],
                "InstanceNo": 1
                }

        podInfos.append(podInfo)

    procInfo = json.dumps({"PodInfos": podInfos})
    path = etcd_lain_apps_path(SERVER_APPNAME, SERVER_PROCTYPE, SERVER_PROCNAME)

    with open(os.devnull, 'w') as FNULL:
        subproc.call(["etcdctl", "set", path, procInfo], stdout=FNULL)

def rm_etcd():
    path = etcd_lain_apps_path(SERVER_APPNAME, SERVER_PROCTYPE, SERVER_PROCNAME)
    with open(os.devnull, 'w') as FNULL:
        subproc.call(["etcdctl", "rm", path], stdout=FNULL)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='set etcd.')
    parser.add_argument('-p', '--port', type=int, default=8081,
                        help='port')
    parser.add_argument('-n', '--amount', type=int, default=1,
                        help='amount')
    args = vars(parser.parse_args())
    print(args)

    rm_etcd()
    set_etcd(args['port'], args['amount'])

    print("set etcd >> done")
