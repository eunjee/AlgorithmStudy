# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:16:44 2021

@author: 조은지
"""
a,b,v=map(int,input().split())

#낮밤
if v%(a-b)!=0:
    one = v//(a-b)+1
else:
    one= v//(a-b)

print(one)
                