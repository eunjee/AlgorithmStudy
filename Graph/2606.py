# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 21:48:12 2022

@author: 조은지
"""
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())

def virous(s):
    q=deque()
    q.append(s)
    visited[s]=True
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i]=True
                q.append(i)

graph=[[] for i in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


virous(1)
print(visited.count(True)-1)