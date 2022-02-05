# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 20:04:16 2021

@author: 조은지
"""
import sys
input = sys.stdin.readline

def find_parent(parent,a):
    if a!=parent[a]:
        parent[a] = find_parent(parent,parent[a])
    return parent[a]

def union(parent,a,b):
    a= find_parent(parent, a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
n,m = map(int,input().split())

parent=[i for i in range(n+1)]

edges=[]
result=0

for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

#간선을 오름차순으로 정렬
edges.sort()

cross=0

#크루스칼 실행
for edge in edges:
    cost, a, b= edge
    if find_parent(parent,a)!=find_parent(parent,b):
        union(parent,a,b)
        result+=cost
        cross=cost

print(result-cross)