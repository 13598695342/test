#!/usr/bin/python
#-*- coding:utf-8 -*-
# # 客户端不需要绑定ip和监听
# import socket
# # 创建一个套接字
# while True:
#     sock=socket.socket()
#     # 客户端不需要绑定ip，只需要建立连接
#     sock.connect(('192.168.2.147',30000))
#     # 发送请求
#     msg=input('>>>')
#     sock.send(msg.encode('utf-8'))
#     reg=sock.recv(1024)
#     print(reg.decode('utf-8'))
# # 断开连接
#     sock.close()
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#使用是udp不需要建立连接，但是不能默认
# host=('127.0.0.1',80)
# msg='nichifanle'
# s.sendto(msg.encode('utf-8'),host)
# reg=s.recv(1024)
# print(reg.decode('utf-8'))


