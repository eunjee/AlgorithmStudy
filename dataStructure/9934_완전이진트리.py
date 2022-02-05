# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 18:18:31 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

k = int(input())
tree= list(map(int,input().split()))
answer=[[] for _ in range(k)]
def inorder(tree,i):
    mid = (len(tree)//2)
    answer[i].append(tree[mid])
    if len(tree)==1:
        return
    inorder(tree[:mid],i+1)
    inorder(tree[mid+1:],i+1)

inorder(tree,0)

for i in range(k):
    print(*answer[i])
    