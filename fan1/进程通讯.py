#!/usr/bin/python
#-*- coding:utf-8 -*-
# # 服务器
# # socket:套接字，提供了通信双方最底层的功能
# # 两个电脑基本功能 发送 接收
# # tcp/ip  通信
# #通过socket使两台主机实现通信
# # server端
# import socket #连接应用层和传输层
# # 创建一个套接字(创建一个有接受能力和发送能力的对象)
# # 默认使用的是tcp:socket.SOCK_STREAM   UDP:socket.SOCK_DGRAM
# # 现在套接字使用的是ipv4和tcp协议
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 绑定ip地址和端口
# s.bind(('192.168.2.231',80))#接受的是一个元组,ip地址为自己主机ip地址
# # 监听服务有没有开启
# s.listen(3)#最大等待个数（奶茶店5个服务员，3个凳子，最大连接数相当于服务员，可以连接5个人，等待数相当于凳子，可以有3个人等）
# while True:
#    # 接受请求
#    # 第一个值，建立连接的信息
#    # 第二个值，客户端的IP地址和端口号
#    client,addr=s.accept()
#    # 接收客户端发送的请求 1024：指的是1024个字节
#    receive=client.recv(1024)
#    print(receive.decode('utf-8'))
#    # 发送响应decode:编码 encode：解码
#    reg=input('>>>')
#    client.send(reg.encode('utf-8'))#在网络传输的过程中不能用字符串
# udp
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('127.0.0.1',80))
# # 第一个参数：客户端的请求
# # 第二个参数：客户端的ip和端口号
# client,addr=s.recvfrom(1024)
# print(client.decode('utf-8'))
# msg='hello'
# s.sendto(msg.encode('utf-8'),addr)
# print(client)



