# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:48:12 2021

@author: 조은지
"""
n = int(input())
li=[]
for i in range(n):
    tmp = int(input())
    li.append(tmp)

li.sort(reverse=True)

answer =0
for i in range(n):
    answer = max(li[i]*(i+1),answer)
print(answer)