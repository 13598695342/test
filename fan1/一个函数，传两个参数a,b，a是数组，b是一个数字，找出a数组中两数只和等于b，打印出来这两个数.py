#!/usr/bin/python
#-*- coding:utf-8 -*-
def hanhan(a,b):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]+a[j]==b:
                print(a[i],a[j])
print(hanhan([12,10,11,13,24],23))
