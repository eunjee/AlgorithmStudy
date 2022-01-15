# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:46:49 2021

@author: 조은지
"""
from collections import deque
import sys
input = sys.stdin.readline

k = int(input())

def bfs(v,color):
    queue = deque()
    queue.append(v)
    colors[v]=color #방문표시
    
    while queue:
        pop = queue.popleft()
        for i in graph[pop]:
            if colors[i]==0:
                queue.append(i)
                colors[i] = -colors[pop]
            elif colors[pop]==colors[i]:
                return False
        
    return True



for i in range(k):
    v,e = map(int,input().split())
    graph = [[] for i in range(v+1)]
    colors = [0]*(v+1)
    
    for j in range(e):
        v1,v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    isBG=True
    for k in range(1,v+1):
        if colors[k]==0:
            if bfs(k,1) is False:
                isBG =False
                break
    
    print("YES" if isBG else "NO")
    