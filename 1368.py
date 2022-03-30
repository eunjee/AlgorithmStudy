#물대기
from heapq import heappush, heappop
#특정 원소가 속한 집합 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n = int(input())
pq=[]
result=0
parent = [i for i in range(n+1)]
#물을 직접 대는 경우
for i in range(1,n+1):
    heappush(pq,[int(input()),0,i]) #0에서 i로 이어진다.

for i in range(1,n+1):
    line = list(map(int,input().split()))
    for j in range(1,n+1):
        if i==j:
            continue
        else:
            heappush(pq,[line[j-1],i,j]) #비용, i에서 j까지

while pq:
    cost,i,j = heappop(pq)
    if find_parent(parent,i)!=find_parent(parent,j):
        result+=cost
        union_parent(parent,i,j)
print(result)