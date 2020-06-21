#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

debug = True
daemon = True
loglevel = 'debug'
bind = '127.0.0.1:9288'
# pidfile = 'log/gunicorn.pid'
# logfile = 'log/debug.log'

#启动的进程数
workers = 2

x_forwarded_for_header = 'X-FORWARDED-FOR'