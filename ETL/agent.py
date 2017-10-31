#!/usr/bin/python
# -*- coding: utf-8 -*-
##连接GUI进行交互
import ETL.common as common

# 建立Linux连接
ssh = common.get_ssh()


# 强制创建ETL信号文件
def force_start_job(sign=''):
    std_in, std_out, std_err = ssh.exec_command("touch /ETL/DATA/receive/%s" % sign)
    for line in std_out.readlines():
        print(line)
    for line in std_err.readlines():
        print(line)


# 正常请求调度任务运行
def invoke_job():
    pass


# 查询Job状态
def query_status():
    pass


# 查看Job日志文件
def get_log_file():
    pass


# 获取Job脚本文件
def get_script_file():
    pass


# 编辑Job脚本文件
def put_script_file():
    pass


if __name__ == '__main__':
    force_start_job('dir.MYSQL_TEST_TABLE20171021')
    ssh.close()
