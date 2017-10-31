#!/usr/bin/python
# -*- coding: utf-8 -*-
##执行Job脚本

import automation.bin.common as common
import automation.bin.MySQL as MySQL

# 建立Linux连接
ssh = common.get_ssh()


##连接至Linux服务器

def send_script_information_log_to_repository():
    pass


def send_Job_information_log_to_repository():
    pass


def invoke_stream_Job():
    pass


def execute_script_file(table_name=''):
    print('Execute the {0} python script.'.format(table_name.replace('\n', '')))
    sys = MySQL.query_sys(table_name)
    script_path = '/ETL/APP/{0}/{1}.py'.format(sys, table_name.lower())
    print('[ Invoke script ] -> ' + script_path)
    return invoke_script(script_path)


def invoke_script(script_path=''):
    std_in, std_out, std_err = ssh.exec_command("python {0}".format(script_path))
    for line in std_out.readlines():
        print('[ Invoke script info ] -> ' + line)
        return True
    for line in std_err.readlines():
        print('[ Invoke script error ] => ' + line)
        return False


def touch_receive_sign(sign):
    # 创建ETL信号文件
    std_in, std_out, std_err = ssh.exec_command("touch /ETL/DATA/receive/%s" % sign)
    for line in std_out.readlines():
        print(line)


if __name__ == '__main__':
    execute_script_file('TEST_TABLE')
