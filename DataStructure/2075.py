# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:28:52 2021

@author: 조은지
"""
import sys
import heapq

input = sys.stdin.readline
max_h = []

n = int(input())

for _ in range(n):
    nums = map(int,input().split())
    
    if not max_h:
        for num in nums:
            heapq.heappush(max_h,num)
    else:
        for num in nums:
            if num>max_h[0]:
                heapq.heappop(max_h)
                heapq.heappush(max_h,num)

print(max_h[0])