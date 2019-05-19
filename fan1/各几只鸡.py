#!/usr/bin/python
#-*- coding:utf-8 -*-
for i in range(1,100):
    for j in range(1,100):
        for d in range(1,100):
            if 2*i+j+0.5*d==100 and i+j+d==100:
                print(i,j,d)


