#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
	word = input()
	if word == "":
		word = "exit"
	sock.send(word.encode())
	data = sock.recv(1024).decode()
	if "EXIT" in data:
		sock.close()
		break
	print(data)
