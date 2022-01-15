# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 21:44:55 2021

@author: 조은지
"""
import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

def bfs(start):
    q= deque()
    visited=[False]*(n+1)
    q.append(start) #출발지 먼저 넣어준다
    
    while q:
        x,y = q.popleft()
        if x==dest[0] and y==dest[1]:
            print("happy") #도착하면 happy~
            return
        for idx, location in enumerate(store): 
            if visited[idx]==False:
                if abs(location[0]-x)+abs(location[1]-y)<=1000:
                    visited[idx]=True
                    q.append(location)
    print("sad")
    return

for i in range(t):
    n = int(input()) #편의점 개수
    #출발지, 편의점+도착, 도착지
    start = list(map(int,input().split()))
    store = [list(map(int,input().split())) for i in range(n+1)]
    dest = store[-1]
    bfs(start)
    