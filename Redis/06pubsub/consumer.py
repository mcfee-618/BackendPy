#coding:utf-8
"""
@author: mcfee
@description:
@file: pubsub.py
@time: 2020/7/24 下午6:52
"""
# -*- coding: utf-8 -*-
import time
import redis

client = redis.StrictRedis()
p = client.pubsub()
p.subscribe("codehole")
while True:
    msg = p.get_message()
    if not msg:
        time.sleep(1)
        continue
    print(msg)