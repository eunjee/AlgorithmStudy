# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 18:24:30 2021

@author: 조은지
"""
import sys
input = sys.stdin.readline
#무한대
INF = int(1e7)
#노드, 간선
n,m = map(int,input().split())

graph=[[INF]*(n+1) for i in range(n+1)]

#자기 자신은 0으로 초기화
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i:
            graph[i][j]=0
        
#친구 입력 받기
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1 #둘은 칭구칭긔

#플로이드 워셜 실행
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

#케빈베이컨수 구하기
min_kb =sum(graph[1][1:])
idx=1
for i in range(2,n+1):
    kb = sum(graph[i][1:])
    if min_kb>kb:
        min_kb= kb
        idx = i
print(idx)
        
    