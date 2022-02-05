# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:54:19 2021

@author: 조은지
"""
from collections import deque
import sys

input = sys.stdin.readline
#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m = map(int,input().split())

visited=[[False]*(m+1) for i in range(n+1)]
#(n+1)*(m+1) 그래프 생성
graph = [[0]*(m+1) for i in range(n+1)]

#그래프 값 넣어주기
for i in range(1,n+1):
    line = input()
    for j in range(m):
        graph[i][j+1]=int(line[j])


def bfs(count):
    q=deque()
    q.append((1,1,count))
    visited[1][1]=True
    
    while q:
        x,y,count = q.popleft()
        for i in range(len(dx)):
            nx=x+dx[i]
            ny=y+dy[i]
            #범위 내 인지 확인
            if nx==n and ny==m:
                return count+1
            if 1<=nx<=n and 1<=ny<=m:
                if visited[nx][ny]==False and graph[nx][ny]==1:
                    q.append((nx,ny,count+1))
                    visited[nx][ny]=True

print(bfs(1))
                    
            
        