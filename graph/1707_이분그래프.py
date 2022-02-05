# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:36:23 2021

@author: 조은지
"""
import sys

sys.setrecursionlimit(100000)

def dfs(start,color):
    colors[start]=color #방문한 노드를 색칠해줌
    
    for i in graph[start]:
        if colors[i]==0:
            if not dfs(i,-color):
                return False
        elif colors[i]==colors[start]:
            return False
        
    return True

k= int(input())

for i in range(k):
    v,e = map(int,sys.stdin.readline().split())
    graph= [[] for i in range(v+1)] #그래프 생성
    colors=[0]*(v+1) #0-방문x, 1검정, -1빨강

    for j in range(e):
        v1,v2 = map(int,sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1) #양방향 그래프
        
    
    #이분그래프인지를 판별
    ok=True
    for i in range(1,v+1):
        if colors[i]==0:
            if dfs(i,1) is False:
                ok=False
                break
    
    print("YES" if ok else "NO")
    

     

                
    
    