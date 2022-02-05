# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 23:07:16 2022

@author: 조은지
"""
from collections import deque
import sys

input = sys.stdin.readline
t = int(input())

def bfs(s):
    q = deque()
    q.append(s) #node,count
    visited[s]=True
    
    count = 0
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
                count+=1
    return count


for _ in range(t):
    n,m = map(int,input().split())
    graph=[[] for i in range(n+1)]
    visited=[False]*(n+1)
    for i in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    answer=0
    for i in range(1,n+1):
        if not visited[i]:
            answer+=bfs(i)
    print(answer)
        