# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:21:15 2021

@author: 조은지
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:06:27 2021

@author: 조은지
"""
import sys
from collections import deque

N=int(input())
M=int(input())


graph=[[] for i in range(N+1)]

for i in range(M):
    v1, v2 = map(int,sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False]*(N+1)


def bfs(v):
    count=0
    queue = deque()
    queue.append(v)
    visited[v]=True
    
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
                count+=1
    return count

print(bfs(1))

    

