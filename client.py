#!/usr/bin/python2
import socket,sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="192.168.10.39"
port=7777
while True:
	message=raw_input('Client: ')
	s.sendto(message,(ip,port))
	t=s.recvfrom(1000)
	print "Received from server: "+t[1]
	
	
	

