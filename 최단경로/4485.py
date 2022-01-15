# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:13:07 2021

@author: 조은지
"""
import heapq
import sys

input = sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1] #상하좌우

INF=int(1e9)

def dijkstra():
    q=[]
    heapq.heappush(q,(graph[0][0],0,0))
    
    while q:
        dist,x,y = heapq.heappop(q) #최소 값을 가진 인덱스 pop
        if x==n-1 and y==n-1:
            print("Problem {0}: {1}".format(count,distance[x][y]))
        
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i] #상하좌우
            
            if 0<=nx<n and 0<=ny<n: #행렬 범위 체크
                cost = dist+graph[nx][ny] #(x,y)노드 거쳐서 (nx,ny)에 갈 때
                if distance[nx][ny] < dist: #이미 방문했었던 노드라면 무시
                    continue
                if cost<distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q,(cost,nx,ny))
                
count=1
while True:
    n = int(input()) #행렬의 크기
    if n==0:
        break
    graph = []
    distance=[[INF]*n for i in range(n)] #2차원 거리 배열
   
    #그래프 입력받기 
    for i in range(n):
        line = list(map(int,input().split()))
        graph.append(line)
    
    #다익스트라 수행
    dijkstra()
    count+=1
    
    