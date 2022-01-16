# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 02:50:25 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[0]*(n+1)]

#입력
for _ in range(n):
    nums = [0]+list(map(int,input().split()))
    graph.append(nums)
#행 별로 더하기
for i in range(1,n+1):
    for j in range(1,n):
        graph[i][j+1]+=graph[i][j]
#열 별로 더하기
for j in range(1,n+1):
    for i in range(1,n):
        graph[i+1][j]+=graph[i][j]

#사각형 빼주기        
for i in range(m):
    x1,y1,x2,y2=map(int,input().split())
    print(graph[x2][y2] - graph[x1 - 1][y2] - graph[x2][y1 - 1] + graph[x1 - 1][y1 - 1])
    