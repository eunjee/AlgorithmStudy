# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 00:32:43 2021

@author: 조은지
"""
from collections import deque
import sys

input = sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

r,c = map(int,input().split())

visited = [[False]*(c) for i in range(r)]
#그래프 입력받기
graph=[]
for i in range(r):
    line = input().rstrip()
    graph.append([])
    for j in line:
        graph[i].append(j)
def bfs(sx,sy):
    q= deque()
    #위치 늑대, 양
    q.append([sx,sy])
    visited[sx][sy]=True
    w=0
    s=0
    while q:
        x,y= q.popleft()
        if graph[x][y]=='v':
            w+=1
        elif graph[x][y]=='k':
            s+=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny]!='#' and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    q.append([nx,ny])
                    
    return w,s

ww=0
ss=0
for i in range(r):
    for j in range(c):
        if visited[i][j]==False and graph[i][j]!='#':
            w,s = bfs(i,j)
            if w>=s:
                ww+=w
            else:
                ss+=s

print(ss,ww)
                