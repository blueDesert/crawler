#!/usr/bin/env python3
import socket
from threading import *

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = '0.0.0.0'
Port = 9000
serv.bind((IP,Port))
serv.listen(5)


while True:
 conn,addr = serv.accept()
 print('client from:',addr)
 while True:
  data=conn.recv(1024)
  if data==b'end\r\n':break
  conn.send(b'data:%s'%(data))
  print(data)
 conn.close()
 print('Client disconnected')


