# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 18:05:29 2021

@author: 조은지
"""
import sys

sys.setrecursionlimit(10**6)

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


t = int(input())
for _ in range(t):
    n = int(input())
    line = list(map(int,input().split()))
    parent = [0]*(n+1)   
    for i in range(len(line)):
        parent[i+1]=line[i]
    count=0
    
    for i in range(1,n+1):
        if find_parent(parent,i)==find_parent(parent,parent[i]):
            count+=1
            continue
    print(n-count)