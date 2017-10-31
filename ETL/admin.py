#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlrd
import xlwt
import tkinter
from tkinter import *
import tkinter.messagebox
import os

# windows_linux交互配置字典
windows_linux_info = {}
windows_linux_info['windows_path'] = 'D:\linux\\test.txt'
windows_linux_info['linux_ip'] = '192.168.1.13'
windows_linux_info['username'] = 'bdetl'
windows_linux_info['password'] = 'huangzhen'
windows_linux_info['linux_path'] = '/home/bdetl/test'
# windows_linux交互配置
password = 'huangzhen'
windows_path = 'D:\linux\\test.txt'
username = 'bdetl'
linux_ip = '192.168.1.13'
linux_path = '/home/bdetl/test'

# 创建列表
oracle = ['table1', 'table2']
sdm = ['s_table1', 's_table2']
fdm = ['f_table1', 'f_table2']


def admin():
    root()


def root():
    # 创建顶层根窗口
    root = tkinter.Tk()
    # 设置顶层窗口属性
    root.title('automation admin')
    root.geometry('600x400')
    # 显示内容
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    menubars(root)
    frames(root)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 显示
    root.mainloop()


def menubars(root):
    ##文件选项
    menubar = Menu(root)
    # 创建下拉菜单file，然后将其加入到顶级的菜单栏中
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="Open", command=hello)
    file_menu.add_command(label="Save", command=hello)
    # 创建下拉菜单的分割线
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=root.quit)
    menubar.add_cascade(label='File', menu=file_menu)
    # 创建connect菜单
    connect_menu = Menu(menubar, tearoff=0)
    connect_menu.add_command(label='Connect to server', command=connect_to_server)
    connect_menu.add_command(label='Connect to ODBC', command=connect_to_ODBC)
    connect_menu.add_command(label='Disconnect', command=disconnect_to_ODBC)
    # 创建option
    menubar.add_cascade(label='Configuration', menu=connect_menu)
    # 创建单选菜单
    menubar.add_command(label='about', command=about)
    # 显示菜单
    root['menu'] = menubar
    # root.config(menu=menubar)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
##automation commands

def windows_to_linux_file(windows_path, linux_path, linux_ip, username, password):
    # 将文件从Windows传到Linux
    print('>>>>>>>>>>>>>>>>>Windows_to_linux_file begin')
    cmd = 'D:\cfg\pscp.exe -pw {password} {windows_path} {username}@{linux_ip}:{linux_path}' \
        .format(password=password, windows_path=windows_path, username=username, linux_ip=linux_ip,
                linux_path=linux_path)
    os.system(cmd)
    print('<<<<<<<<<<<<<<<<<Windows_to_linux_file end.')


def windows_to_linux_dir(windows_path, linux_path, linux_ip, username, password):
    # 将文件夹从Windows传到Linux
    print('>>>>>>>>>>>>>>>>>Windows_to_linux_dir begin')
    cmd = 'D:\cfg\pscp.exe -pw {password} -r {windows_path} {username}@{linux_ip}:{linux_path}' \
        .format(password=password, windows_path=windows_path, username=username, linux_ip=linux_ip,
                linux_path=linux_path)
    os.system(cmd)
    print('<<<<<<<<<<<<<<<<<Windows_to_linux_dir end')


def connect_to_server():
    # tkinter.messagebox.showinfo('Connect information', 'Function: connect to the server.')
    master = Tk()
    master.title('Server information')
    master.geometry('300x300')
    # windows_path
    Label(master, text='windows_path: ').pack()
    windows_path_text = StringVar()
    windows_path_value = Entry(master, textvariable=windows_path_text)
    windows_path_text.set(' ')
    windows_path_value.pack()
    # linux_ip
    Label(master, text='linux_ip: ').pack()
    linux_ip_text = StringVar()
    linux_ip_value = Entry(master, textvariable=linux_ip_text)
    linux_ip_text.set(' ')
    linux_ip_value.pack()
    # username
    Label(master, text='username: ').pack()
    username_text = StringVar()
    username_value = Entry(master, textvariable=username_text)
    username_text.set(' ')
    username_value.pack()
    # password
    Label(master, text='password: ').pack()
    password_text = StringVar()
    password_value = Entry(master, textvariable=password_text)
    password_text.set(' ')
    password_value.pack()
    # linux_path
    Label(master, text='linux_path: ').pack()
    linux_path_text = StringVar()
    linux_path_value = Entry(master, textvariable=linux_path_text)
    linux_path_text.set(' ')
    linux_path_value.pack()

    # press
    def connect_to_server_press():
        windows_linux_info['windows_path'] = a = windows_path_text.get()
        windows_linux_info['linux_ip'] = b = linux_ip_text.get()
        windows_linux_info['username'] = c = username_text.get()
        windows_linux_info['password'] = d = password_text.get()
        windows_linux_info['linux_path'] = e = linux_path_text.get()
        string = str("windows_path: %s\nlinux_ip: %s\nusername: %s\npassword: %s\nlinux_path: %s\n" % (
        windows_linux_info['windows_path'], windows_linux_info['linux_ip'], windows_linux_info['username'],
        windows_linux_info['password'], windows_linux_info['linux_path']))
        print('Msg: ' + a + b + c + d + e)
        tkinter.messagebox.showinfo(title='infomation', message=string)

    Button(master, text='update', command=connect_to_server_press).pack()


def disconnect_to_ODBC():
    tkinter.messagebox.showinfo('ODBC information', 'Disconnected.')


def connect_to_ODBC():
    tkinter.messagebox.askokcancel('check', 'Do you want to connect the ODBC?')


def hello():
    print('hello')
    tkinter.messagebox.showinfo('Say hi', 'Welcome to use automation!')


def about():
    tkinter.messagebox.showinfo('author information', 'huang zhen\n raystel@icloud.com')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def frames(root):
    ##框架
    top_box = Frame(root, borderwidth=3)
    Label(top_box, text='automation', bg='green', width=100).pack()
    top_box.pack()


def shortcut_bar(root):
    ##快捷操作栏设置
    # 快捷操作栏内容
    shortcut = ['connect', 'disconnect', 'refresh']
    # 显示快捷操作栏
    for button in shortcut:
        tkinter.Button(root, text=button).pack(side='left')

        ##输入框
        # 定义输入框内容


def top():
    top = tkinter.Tk()
    top.mainloop()


def automation():
    admin()


def readMsg():
    pass


if __name__ == '__main__':
    automation()
