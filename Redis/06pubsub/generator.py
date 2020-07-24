#coding:utf-8
"""
@author: mcfee
@description:
@file: generator.py
@time: 2020/7/24 下午6:53
"""
import redis

client = redis.StrictRedis()
client.publish("codehole", "python comes")
client.publish("codehole", "java comes")
client.publish("codehole", "golang comes")