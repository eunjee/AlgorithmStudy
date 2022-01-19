# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 22:25:20 2022

@author: 조은지
"""
import sys
import copy
from collections import deque

input = sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1] #상하좌우
n,m = map(int,input().split())
graph = [list(map(int,input().rstrip().split())) for i in range(n)]

answer=0
#bfs
def spread_virus():
    global answer
    q= deque()
    visited=copy.deepcopy(graph)
    v_count=0
    #2인 값들 데크에 넣기
    for i in range(n):
        for j in range(m):
            if visited[i][j]==2:
                q.append((i,j)) #위치 넣기
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0:
                    visited[nx][ny]=2
                    q.append((nx,ny))
                    
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0:
                v_count+=1
    answer=max(answer,v_count)
                
    

#벽 3개 선택
def select_wall(count):
    if count==3:
        spread_virus()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                select_wall(count+1)
                graph[i][j]=0

select_wall(0)
print(answer)