# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:07:42 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

answer=0
tmp=0

for i in range(n-1):
    if price[tmp]>price[i+1]:
        answer+=price[tmp]*distance[i]
        tmp=i+1
    else:
        answer+=price[tmp]*distance[i]
        
print(answer)