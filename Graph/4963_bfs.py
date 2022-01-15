# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:19:40 2021

@author: 조은지
"""
#섬의 개수
from collections import deque
import sys

input = sys.stdin.readline

dx=[1, 1, 0, -1, -1, -1, 0, 1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]

def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y]=True
    
    while queue:
        px,py = queue.popleft()
        for i in range(len(dx)):
            nx = px+dx[i]
            ny = py+dy[i]
            if nx<0 or nx>=h or ny<0 or ny>=w:
                continue
            elif graph[nx][ny]==1 and visited[nx][ny]==False:
                queue.append([nx,ny])
                visited[nx][ny]=True
            


while True:
    w, h = map(int,input().split()) #너비 높이
    graph=[]
    
    if w==0 and h==0: # 0 0을 받으면 종료
        break
    visited = [[False]*w for i in range(h)]
    
    for i in range(h):
        line = list(map(int, input().split()))
        graph.append(line)
        
    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and visited[i][j]==False:
                bfs(i,j)
                answer+=1
    
    print(answer)