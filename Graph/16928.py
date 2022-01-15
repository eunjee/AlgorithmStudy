# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:57:32 2021

@author: 조은지
"""
from collections import deque
import sys

input = sys.stdin.readline

#101짜리 일차원 게임판 생성
game = [0 for i in range(101)]

#사다리, 뱀의 개수
l,s = map(int,input().split())

#사다리 위치 입력받기
for _ in range(l):
    x,y = map(int,input().split())
    #x번째 사다리에 도착하면 y로 간다
    game[x]=y

#뱀의 위치 입력받기
for _ in range(s):
    u,v = map(int,input().split())
    game[u]=v

dx=[1,2,3,4,5,6]
def bfs():
    q = deque()
    visited =[False]*101
    #[위치, count]
    q.append([1,0])
    visited[1]=True
    
    while q:
        now,count= q.popleft()
        if now==100:
            return count
        else:
            for x in dx:
                nx=now+x
                if nx>100: #100넘으면 안된다.
                    continue
                elif game[nx]!=0: #뱀이나 사다리 걸리면
                    if visited[game[nx]]==False:
                        q.append([game[nx],count+1])
                        visited[game[nx]]==True
                else:#그냥 이동이면?
                    if visited[nx]==False:
                        q.append([nx,count+1])
                        visited[nx]=True
                        
print(bfs())
                