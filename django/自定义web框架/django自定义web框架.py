#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
def handel_request(client):
    buf=client.recv(1024)
    client.send(b"HTTP/1.1 200 OK\r\n\r\n")
    client.send(b"Hello, Seven")

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("localhost",8099))
    sock.listen(5)

    while True:
        connection,address=sock.accept()
        handel_request(connection)
        connection.close()

if __name__ == '__main__':
    main()