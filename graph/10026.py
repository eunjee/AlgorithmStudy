# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:37:36 2021

@author: 조은지
"""
from collections import deque
import sys

input = sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n= int(input())
graph = [[0]*(n+1) for i in range(n+1)]
visited=[[False]*(n+1) for i in range(n+1)]

#그래프 값 넣어주기
for i in range(1,n+1):
    line = input()
    for j in range(n):
        graph[i][j+1]=line[j]

#색약 아닌 사람
def bfs(sx,sy):
    q= deque()
    q.append([sx,sy])
    visited[sx][sy]=True
    
    while q:
        x,y = q.popleft()
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<nx<=n and 0<ny<=n:
                if graph[nx][ny]==graph[x][y] and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    q.append([nx,ny])
    return 



count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if visited[i][j]==False:
            count+=1
            bfs(i,j)
print(count,end=" ")

#G를 R로 바꾸기
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]=='G':
            graph[i][j]='R'

visited=[[False]*(n+1) for i in range(n+1)]
count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if visited[i][j]==False:
            count+=1
            bfs(i,j)           
print(count)
    