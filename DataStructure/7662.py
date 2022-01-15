# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 18:11:09 2021

@author: 조은지
"""
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    min_h= []
    max_h = []
    k = int(input())
    visited=defaultdict(int)
    for i in range(k):
        op,num = input().rstrip().split()
        if op =='I':
            heapq.heappush(min_h,int(num))
            heapq.heappush(max_h,-1*int(num))
            visited[int(num)]+=1
        else:
            if num == '-1': #최솟값
                while min_h and not visited[min_h[0]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0]]-=1
                    heapq.heappop(min_h)
            else:
                while max_h and not visited[-1*max_h[0]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[-1*max_h[0]]-=1
                    heapq.heappop(max_h)
                
    while max_h and not visited[-1*max_h[0]]:
        heapq.heappop(max_h)
    while min_h and not visited[min_h[0]]:
        heapq.heappop(min_h)
    if len(max_h)==0:
        print("EMPTY")
    else:
        print(-1*max_h[0],min_h[0])