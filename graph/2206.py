# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:22:42 2021

@author: 조은지
"""
from collections import deque
import sys

input = sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m = map(int,input().split())

graph=[]

#그래프 입력받기
for i in range(n):
    graph.append([])
    arr = input().rstrip()
    for j in range(m):
        graph[i].append(int(arr[j]))
        
        
def bfs(sx,sy):
    q = deque()
    visited=[[[False]*2 for i in range(m)] for j in range(n)]
    #x,y,flag,count
    q.append([sx,sy,0,1])
    visited[sx][sy][0]=True
    
    while q:
        x,y,w,count = q.popleft()
        if x==n-1 and y==m-1:
            return count
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny][w]==False:
                    if graph[nx][ny]==0:
                        q.append([nx,ny,w,count+1])
                        visited[nx][ny][w]=True
                    else:
                        if w==0:
                            q.append([nx,ny,1,count+1])
                            visited[nx][ny][1]=True
    
    return -1

print(bfs(0,0))
        