#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/24 19:45
# @Author  : Aries
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8080))
while True:
    msg = input(">>")
    if not msg:continue
    client.send(msg.encode("utf-8"))
    server_msg=client.recv(1024)
    print(server_msg.decode("utf-8"))
client.close()