# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 18:21:00 2021

@author: 조은지
"""
import sys

sys.setrecursionlimit(10000)

n,m= map(int, sys.stdin.readline().split())

graph=[[] for i in range(n+1)] 

visited=[False]*(n+1)

for i in range(m):
    s,e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s) #양방향

def dfs(v):
    visited[v]=True 
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

answer=0

for idx in range(1,n+1):
    if not visited[idx]:
        dfs(idx)
        answer+=1

    
print(answer)
