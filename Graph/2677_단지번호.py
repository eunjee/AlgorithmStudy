# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 16:02:33 2021

@author: 조은지
"""
import sys

sys.setrecursionlimit(10000)

dx=[-1,1,0,0]
dy=[0,0,-1,1]


N = int(input())

visited=[[False]*N for i in range(N)]

graph=[]

count=1

for i in range(N):
    line = map(int, input())
    graph.append([])
    for v in line:
        graph[i].append(v)

def dfs(x,y,count):
    visited[x][y]=True
    for i in range(len(dx)):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0 <= nx <N and 0<= ny <N:
            if visited[nx][ny]==False and graph[nx][ny]==1:
                count = dfs(nx,ny,count+1)
    return count            
        
            

result=[]
for i in range(N):
    for j in range(N):
        if visited[i][j]==False and graph[i][j]==1:
            result.append(dfs(i,j,1))

print(len(result))
result.sort()
for i in result:
    print(i)
