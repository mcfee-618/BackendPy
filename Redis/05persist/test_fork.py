# coding:utf-8
"""
@author: mcfee
@description:
@file: test_fork.py
@time: 2020/6/29 上午11:47
"""
import os

value = 2

if (os.fork() > 0):
    value = 3
    print("父进程{0}".format(value))
else:
    # 子进程继承了父进程的数据段
    print("子进程{0}".format(value))
