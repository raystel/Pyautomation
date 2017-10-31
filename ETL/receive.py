#!/usr/bin/python
# -*- coding: utf-8 -*-
# 监控/ETL/DATA/receive
import string
import time
import ETL.common as common
import ETL.MySQL as MySQL

# 建立Linux连接
ssh = common.get_ssh()


def __check_receive_sign():
    # 获取信号文件,如果在Job有定义，并且处于启用状态，则将信号发送至queue列队，否则发送至fail列队
    print("[>>>>>>>] -> Scan /ETL/DATA/receive")
    # 假如文件夹不存在,则创建文件夹/ETL/DATA/receive
    std_in, std_out, std_err = ssh.exec_command("ls /ETL/DATA/receive")
    for sign in std_out.readlines():
        sign = sign.replace('\n', '')
        print('[ INFO  ] -> Receive the signal: ' + sign)
        job_sys, job_name = __get_job_name(sign)
        if __defined(job_name):
            if __enable(job_name):
                __move_to_queue(sign)
            else:
                __move_to_fail_unable(sign)
        else:
            __move_to_fail_undefined(sign)
    for sign in std_err.readlines():
        print('[ ERROR ] => Get receive signal error: ' + sign)
    print('[<<<<<<<] -> Scanned.')


def __move_to_fail_undefined(sign):
    print('[ ERROR ] => Send {0} to /ETL/DATA/fail/undefined.\n'.format(sign))
    std_in, std_out, std_err = ssh.exec_command('mv /ETL/DATA/receive/{0} /ETL/DATA/fail/undefined/{0}'.format(sign))
    for info in std_out.readlines():
        print('[ INFO  ] -> ' + info)
    for error in std_err.readlines():
        print('[ ERROR ] => ' + error)


def __move_to_fail_unable(sign):
    print('[ ERROR ] => Send {0} to /ETL/DATA/fail/unable.\n'.format(sign))
    std_in, std_out, std_err = ssh.exec_command('mv /ETL/DATA/receive/{0} /ETL/DATA/fail/unable/{0}'.format(sign))
    for info in std_out.readlines():
        print('[ INFO  ] -> ' + info)
    for error in std_err.readlines():
        print('[ ERROR ] => ' + error)


def __move_to_queue(sign):
    queue_sign = sign.split('.')[1] + '.queue'
    print('[ INFO  ] -> touch /ETL/DATA/queue/{0}'.format(queue_sign))
    print('[ INFO  ] -> move {0} to /ETL/DATA/fail/unable/{1}.\n'.format(sign, queue_sign))
    std_in, std_out, std_err = ssh.exec_command('mv /ETL/DATA/receive/{0} /ETL/DATA/queue/{1}'.format(sign, queue_sign))
    for info in std_out.readlines():
        print('[ INFO  ] -> ' + info)
    for error in std_err.readlines():
        print('[ ERROR ] => ' + error)


def __defined(table_name):
    if MySQL.query_job_exist(table_name):
        print('[ INFO  ] -> {0} is defined.'.format(table_name))
        return True
    else:
        print('[ ERROR ] => {0} is not in repository.'.format(table_name))
        return False


def __enable(job_name):
    enable_value = MySQL.query_enable(job_name)
    if enable_value:
        print('[ INFO  ] -> The job {0} is enable.'.format(job_name))
    else:
        print('[ INFO  ] -> The job {0} was baned.'.format(job_name))
    return enable_value


def __get_job_name(sign):
    job_sys = job_name = ''
    try:
        job_name = sign.split('.')[1][0:-1].rstrip(string.digits).split('_', 1)[1]
        job_sys = sign.split('.')[1][0:-1].rstrip(string.digits).split('_', 1)[0]
    finally:
        print('[ INFO  ] -> Job system is {0}, and the job name is {1}'.format(job_sys, job_name))
        return job_sys, job_name


def calendar():
    pass


def convert_name():
    pass


def record_to_repository():
    pass


def receive_start():
    try:
        while True:
            __check_receive_sign()
            time.sleep(10)
    finally:
        ssh.close()


if __name__ == '__main__':
    try:
        while True:
            __check_receive_sign()
            print('!!!!!!!!sleep 10s')
            time.sleep(10)
    finally:
        ssh.close()
