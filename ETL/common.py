#!/usr/bin/python
# -*- coding: utf-8 -*-
# 连接GUI进行交互
import configparser
import paramiko

# 读取基本配置文件
config = configparser.ConfigParser()
config.read(r"C:\Users\93284\PycharmProjects\Pyautomation\ETL\automation.ini")
# 读取配置
LINUX_IP = config.get('Linux', 'ip')
LINUX_USR = config.get('Linux', 'username')
LINUX_PASSWORD = config.get('Linux', 'password')
LINUX_FTP_PORT = config.get(r'Linux', r'ftp_port')
# 连接至Linux服务器
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(LINUX_IP, 22, LINUX_USR, LINUX_PASSWORD)


def get_ssh():
    return ssh


if __name__ == '__main__':
    print(LINUX_IP)
