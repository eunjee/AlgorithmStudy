# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 00:16:39 2021

@author: 조은지
"""
from collections import deque
import sys

sys.setrecursionlimit(10000)

dx=[1, 1, 0, -1, -1, -1, 0, 1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]

def dfs(x,y):
    visited[x][y]=True
    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=h or ny<0 or ny>=w:
           continue
        elif graph[nx][ny]==1 and visited[nx][ny]==False:
            dfs(nx,ny)
             
            

while 1:
    w, h = map(int,input().split())
    graph=[]
    if w==0 and h==0:
        break
    visited = [[False]*w for i in range(h)]
    for i in range(h):
        line = list(map(int, input().split()))
        graph.append(line)
    
    answer =0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and visited[i][j]==False:
                dfs(i,j)
                answer+=1
    print(answer)
        

