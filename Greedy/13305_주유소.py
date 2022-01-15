# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:53:26 2021

@author: 조은지
"""
n = int(input())
distance = list(map(int,input().split()))
prices = list(map(int,input().split()))

answer =0
tmp=0

for i in range(n-1):
    if prices[tmp]>prices[i+1]:
        answer+=prices[tmp]*distance[i]
        tmp=i+1#다음 주유소 갈 때 까지만
    else:
        answer+=prices[tmp]*distance[i]
print(answer)

