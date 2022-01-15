# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 21:08:25 2021

@author: 조은지
"""
import sys

input = sys.stdin.readline
INF=int(1e9)


#테스트 케이스 개수 입력
t = int(input())

for i in range(t):
    n = int(input()) #편의점 개수
    location = [list(map(int,input().split())) for j in range(n+2)]
    graph=[[INF]*(n+2) for i in range(n+2)]
    
    for i in range(n+2):
        for j in range(n+2):
            if i==j:
                graph[i][j]=0
                continue
            if abs(location[i][0]-location[j][0])+abs(location[i][1]-location[j][1])<=1000:
                graph[i][j]=1 #1000m 내에 있다면 경유할 수 있음

    for k in range(n+2):
        for a in range(n+2):
            for b in range(n+2):
                graph[a][b]= min(graph[a][b],graph[a][k]+graph[k][b])
    
    if graph[0][n+1]==INF:
        print("sad")
    else:
        print("happy")