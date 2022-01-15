# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:05:48 2021

@author: 조은지
"""
from collections import deque
import copy
import sys

input = sys.stdin.readline
#테스트 케이스 개수
t = int(input())

def topology_sort(target):
    q= deque()
    result = copy.deepcopy(times)
    #진입차수 0인 건물 큐에 삽입
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            indegree[i]-=1
            result[i-1] = max(result[i-1],result[now-1]+times[i-1])
            if indegree[i]==0:
                q.append(i)

    print(result[target-1])
    return
        


for _ in range(t):
    v,e = map(int,input().split())
    #times만 인덱스 0부터 시작
    times=list(map(int,input().split()))
    indegree=[0]*(v+1)
    graph = [[] for i in range(v+1)]
    
    for i in range(1,v+1):
        graph[i].sort()
    
    for _ in range(e):
        a,b = map(int,input().split())
        indegree[b]+=1
        graph[a].append(b)
    
    target = int(input())
    topology_sort(target)
    
    