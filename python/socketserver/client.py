#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/4 9:17
# @Author  : Aries
# @Site    : 
# @File    : client.py
# @Software: PyCharm
from socket import *
client=socket(AF_INET,SOCK_STREAM)
client.connect(("127.0.0.1",8080))
while True:
    msg=input(">>:").strip()
    if not msg:continue
    client.send(msg.encode("utf-8"))
    data=client.recv(1024)
    print(data.decode("utf-8"))