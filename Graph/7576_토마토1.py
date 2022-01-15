# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:43:48 2021

@author: 조은지
"""
from collections import deque
M,N = map(int, input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

count=0
tomato=[]
queue= deque()
def bfs():
    while queue:
        x,y = queue.popleft()
        
        for k in range(len(dx)):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if tomato[nx][ny]==0:
                    tomato[nx][ny]= tomato[x][y]+1
                    queue.append([nx,ny])
                    
    return tomato

#토마토 맵 입력받기
for i in range(N):
    line = list(map(int,input().split()))
    tomato.append(line)
    for idx,t in enumerate(line):
        if t==1:
            queue.append([i,idx]) #익은 토마토의 위치를 저장


tomato = bfs()

answer=0

#토마토 탐색
for line in tomato:
    for t in line:
        if t == 0:
            print(-1)
            exit(0)
        else:
            answer = max(answer,t)
            
print(answer-1)
