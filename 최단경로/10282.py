# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:52:20 2021

@author: 조은지
"""
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
#테케 개수 입력
t = int(input())

def dijkstra(start):
    q=[]
    visited[start]=True
    dist[start]=0
    heapq.heappush(q,(0,start))#dist,node
    
    while q:
        distance, node = heapq.heappop(q) #노드 선택
        if dist[node] < distance: #이미 방문했었던 노드라면 무시
            continue
        
        for i in graph[node]:
            cost = distance+i[1] #노드를 거쳐갔을 때의 비용
            if cost<dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

for _ in range(t):
    n,d,c = map(int,input().split())
    graph = [[] for i in range(n+1)]
    visited=[False]*(n+1)
    dist=[INF]*(n+1)
    
    #간선 개수만큼 입력
    for i in range(d):
        a,b,s = map(int,input().split())
        graph[b].append([a,s])
    
    #다익스트라 실행
    dijkstra(c)
    #개수
    count = n-dist.count(INF)+1
    
    #걸린 비용 탐색
    time=0
    for i in range(1,n+1):
        if dist[i]==INF:
            continue
        else:
            if time<dist[i]:
                time=dist[i]
    print(count,time)
    