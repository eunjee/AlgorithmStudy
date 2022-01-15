# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 17:15:51 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline
INF = int(1e9)

def dfs(k,n):
    if k>=n:
        return 
    for i in range(n):
        if tree[i]==k:
            tree[i]=INF
            dfs(i,n)
    return


n = int(input())
tree = list(map(int,input().split()))

k = int(input()) #삭제할 노드

tree[k] = INF

dfs(k,n)
count=0
#리프노드 개수 구하기
for i in range(n):
    if tree.count(i)==0 and tree[i]!=INF:
        count+=1
print(count)