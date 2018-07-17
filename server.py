#!/usr/bin/python2
import socket,sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.10.39",7777))
while True:
	data=s.recvfrom(1000)
	print data
	reply=raw_input('server: ')
	client_address=data[1]
	s.sendto(reply,client_address)

