# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 19:00:47 2021

@author: 조은지
"""
import sys

input = sys.stdin.readline
INF = int(1e9)

#정점의 개수
n = int(input())

#인접행렬 받아오기
graph = [list(map(int,input().split())) for i in range(n)]

#플로이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k]==1 and graph[k][j]==1:
                graph[i][j]=1

for i in range(n):
    for j in range(n):
        print(graph[i][j],end=" ")
    print()