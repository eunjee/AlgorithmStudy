# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 21:49:38 2021

@author: 조은지
"""
from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def baechu(sx,sy):
    q = deque()
    q.append([sx,sy])
    visited[sx][sy]=True
    
    while q:
        x,y = q.popleft()
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1:
                    if visited[nx][ny]==False:
                        q.append([nx,ny])
                        visited[nx][ny]=True
            
    
for _ in range(t):
    m,n,k = map(int,input().split())
    graph =[[0]*m for i in range(n)]
    visited=[[False]*(m) for i in range(n)]
    #입력받기
    for i in range(k):
        a,b = map(int,input().split())
        graph[b][a]=1
        
    count=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                if visited[i][j]==False:
                    baechu(i, j)
                    count+=1
    print(count)
    
        