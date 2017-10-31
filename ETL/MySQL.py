#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql
import configparser

# 读取配置
config = configparser.ConfigParser()
config.read(r"C:\Users\93284\PycharmProjects\Pyautomation\bin\automation.ini")
IP = config.get("MySQL", "ip")
MySQL_user = config.get("MySQL", "username")
MySQL_password = config.get("MySQL", "password")
MySQL_database = config.get("MySQL", "database")
# MySQL配置
conn = pymysql.connect(user=MySQL_user, passwd=MySQL_password, host=IP, db=MySQL_database)
cur = conn.cursor()


# 执行SQL语句

def query_status():
    pass


def query_enable(job_name):
    res = cur.execute("SELECT enable FROM ETL.ETL_Job WHERE ETL_Job='{0}'".format(job_name))
    print("[ MSG   ] >> SELECT enable FROM ETL.ETL_Job WHERE ETL_Job='{0}'".format(job_name))
    print("[ MSG   ] >> The enable value of the {0} is {1}".format(job_name, res))
    return res


def query_job_exist(job_name):
    res = cur.execute("SELECT * FROM ETL.ETL_Job WHERE ETL_Job='{0}'".format(job_name))
    return res


def query_sys(job_name):
    print("[ MSG   ] >> SELECT sys FROM ETL.ETL_Job WHERE ETL_Job='{0}'".format(job_name))
    cur.execute("SELECT sys FROM ETL.ETL_Job WHERE ETL_Job='{0}'".format(job_name))
    sys = ''.join(cur.fetchone())
    print('[ MSG   ] >> The system of the {0} is {1}.'.format(job_name, sys))
    return sys


if __name__ == '__main__':
    query_sys('TEST_TABLE')
    cur.close()
    conn.close()
