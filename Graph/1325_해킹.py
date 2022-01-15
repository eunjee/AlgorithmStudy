# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:06:27 2021

@author: 조은지
"""
import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())


graph=[[] for i in range(N+1)]

for i in range(M):
    v1, v2 = map(int,sys.stdin.readline().split())
    graph[v2].append(v1)

answers=[]

def bfs(v):
    count=1
    queue = deque()
    queue.append(v)
    visited = [False]*(N+1)
    visited[v]=True
    
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
                count+=1
    return count

for i in range(1,N+1):
    answers.append(bfs(i))
    
max_cnt=max(answers)

for i,answer in enumerate(answers):
    if max_cnt==answer:
        print(i+1,end=' ')
        