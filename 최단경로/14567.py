# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:35:12 2021

@author: 조은지
"""
from collections import deque
import sys

input = sys.stdin.readline

#노드 간선 입력
v,e = map(int,input().split())

#진입차수, 학기수 리스트
indegree=[0]*(v+1)
total = [1]*(v+1)

#그래프
graph = [[] for i in range(v+1)]

#입력받기
for _ in range(e):
    a,b = map(int, input().split())
    indegree[b]+=1 #진입차수 +1
    graph[a].append(b)

def topology_sort():
    q = deque()
    
    #진입차수 0인 노드 넣기
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    
    #탐색
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i]-=1 #간선 끊기
            if indegree[i]==0:
                total[i] = total[now]+1
                q.append(i)

topology_sort()

for t in total[1:]:
    print(t, end=" ")
                