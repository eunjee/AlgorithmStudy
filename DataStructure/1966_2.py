# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:57:20 2021

@author: 조은지
"""
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n,m = map(int,input().split())
    priority = deque(input().split()) #중요도
    idx = deque(range(n))        #인덱스
    count=1
    while True:
        if priority[0]==max(priority):
            if idx[0]==m:
                print(count)
                break
            else:
                priority.popleft()
                idx.popleft()
                count+=1
        else:
            priority.rotate(-1)
            idx.rotate(-1)

