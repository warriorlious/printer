#!/usr/bin/python

import socket
import thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 5000))

i = 0
f = open("/home/pi/printer/test.txt", "r+") 
server.listen(5)

def handler(client, addr):
	print ' client accepted'
	while True:
		data = client.recv(2048)
		if not data:
			break
		f.write(str(data))
print 'listening...'
while True:
	conn, addr = server.accept()
	thread.start_new_thread(handler, (conn, addr))
