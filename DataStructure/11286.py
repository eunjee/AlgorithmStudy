# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:20:41 2022

@author: 조은지
"""
import heapq
import sys

input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    x = int(input())
    if x==0:
        if len(h)==0:
            print(0)
        else:
            a,b = heapq.heappop(h)
            print(b)
    else:
        heapq.heappush(h,(abs(x),x))
    
    