# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 20:12:02 2022

@author: 조은지
"""
import sys
import heapq

input = sys.stdin.readline

n,k = map(int,input().split())

val=[]
for _ in range(n):
    heapq.heappush(val,list(map(int,input().rsplit()))) #무게를 기준으로 minHeap
    
cval = []
for _ in range(k):
    cval.append(int(input()))

cval.sort()

answer=0
tmp=[]

for c in cval:
    while val and c>=val[0][0]:
        heapq.heappush(tmp, -heapq.heappop(val)[1])
    
    if tmp:
        answer-=heapq.heappop(tmp)

print(answer)
    
        