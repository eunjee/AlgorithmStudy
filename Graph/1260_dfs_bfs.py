# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 17:32:49 2021

@author: 조은지
"""
from collections import deque

n,m,start = map(int, input().split())

graph=[[] for i in range(n+1)] 

visited=[False]*(n+1)

for i in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s) #양방향

for line in graph:
    line.sort()
    
#dfs 함수
def dfs(start):
    visited[start]=True
    print(start, end=' ')
    
    for v in graph[start]:
        if visited[v]==False:
            dfs(v)

#bfs 함수
def bfs(start):
    queue = deque()
    visited[start] = True
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if visited[i]==False:
                visited[i]=True
                queue.append(i)
            
dfs(start)

visited=[False]*(n+1)
print()
bfs(start)
