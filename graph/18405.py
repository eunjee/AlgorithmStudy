# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:48:52 2021

@author: 조은지
"""
from collections import deque
import sys

input = sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,k = map(int,input().split())

#지도 입력
graph=[list(map(int,input().split())) for _ in range(n)]

s, x, y = map(int,input().split())

virus=[]

for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            virus.append((graph[i][j],i,j,0))

#바이러스 번호를 기준으로 정렬
virus.sort()

def spread_virus():
    q=deque(virus)
    #바이러스를 큐에 넣는다. 
    
    while q:
        num,sx,sy,time = q.popleft()
        if time==s:
            break
        for i in range(4):
            nx = sx+dx[i]
            ny = sy+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=num
                    q.append((num,nx,ny,time+1))
                    

spread_virus()
print(graph[x-1][y-1])

    