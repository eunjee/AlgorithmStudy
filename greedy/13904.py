# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 18:38:43 2022

@author: 조은지
"""
import sys
import heapq

input = sys.stdin.readline
n = int(input())

heap = []

for _ in range(n):
    d,w = map(int,input().split())
    heapq.heappush(heap,(-w,d)) #점수를 기준으로 최대힙

work = [0]*(1000+1)

for i in range(n):
    w,d = heapq.heappop(heap)
    for j in range(d,0,-1):
        if work[j]==0:
            work[j] = -w
            break

print(sum(work))