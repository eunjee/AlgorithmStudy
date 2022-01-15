# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 19:08:01 2021

@author: 조은지
"""
import sys
input = sys.stdin.readline
n = int(input().rstrip())
count=1
num =[]
answer = []
flag=0
for _ in range(n):
    k = int(input().rstrip())
    while count<=k:
        num.append(count)
        count+=1
        answer.append('+')
        
    if num[-1]==k:
        num.pop()
        answer.append('-')
    else:
        print('NO')
        flag=1
        break
        
if flag==0:
    for a in answer:
        print(a)