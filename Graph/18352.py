# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:28:40 2021

@author: 조은지
"""
from collections import deque
import sys

input = sys.stdin.readline
#input
n,m,k,x = map(int,input().rstrip().split())

graph = [[] for i in range(n+1)]
answers=[]
def check_distance(x):
    q = deque()
    visited=[False]*(n+1)
    #노드와 거리
    q.append([x,0])
    visited[x]=True
    while q:
        now,count = q.popleft()
        if count==k:
            answers.append(now)
            continue
        for i in graph[now]:
            if not visited[i]:
                visited[i]=True
                q.append([i,count+1])
                
for _ in range(m):
    s,e = map(int,input().rstrip().split())
    graph[s].append(e) #단방향

check_distance(x)
if len(answers)==0:
    print(-1)
else:
    answers.sort()
    for a in answers:
        print(a)