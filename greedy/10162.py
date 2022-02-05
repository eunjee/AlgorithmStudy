# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:31:33 2021

@author: 조은지
"""
n = int(input())

button = [300,60,10]
result = []
for b in button:
    result.append(n//b)
    n%=b

if n!=0:
    print(-1)
else:
    for r in result:
        print(r,end=" ")