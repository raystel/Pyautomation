#!/usr/bin/python
# -*- coding: utf-8 -*-
# 监控/ETL/DATA/queue
import string
import automation.bin.common as common
import automation.bin.MySQL as MySQL

# 建立Linux连接
ssh = common.get_ssh()


def check_queue_signal():
    # 扫描信号文件，检查依赖是否完成，所有依赖完成则放入process
    print("[>>>>>>>] -> Scan /ETL/DATA/queue")
    std_in, std_out, std_err = ssh.exec_command("ls /ETL/DATA/queue")
    for sign in std_out.readlines():
        sign = sign.replace('\n', '')
        print('[ INFO  ] -> Receive the signal in queue: {0}'.format(sign))
        job_name=get_job_name(sign)
        dependencies_list= status_of_dependence(job_name)
        for dependence in dependencies_list:
            print(dependence)
            pass

    for sign in std_err.readlines():
        print('[ ERROR ] => Get queue signal error: {0}'.format(sign))

def status_of_dependence(job_name):
    #查询Job依赖
    print(job_name)
    return []


def get_job_name(sign):
    print('[ INFO  ] -> Job name is {0}'.format(sign.split('.')[0].split('_',1)[1][0:-1].rstrip(string.digits)))
    return sign.split('.')[0].split('_',1)[1][0:-1].rstrip(string.digits)


def enable(job_name):
    enable_value = MySQL.query_enable(job_name)
    return enable_value


def dependencies_finish():
    pass


def in_limited_concurrence():
    pass


if __name__ == '__main__':
    check_queue_signal()
