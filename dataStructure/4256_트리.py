# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 23:18:16 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

def toPostorder(preorder,inorder):
    if len(preorder)==1:
        print(preorder[0],end=" ")
        return
    elif len(preorder)==2:
        print(preorder[1],preorder[0],end=" ")
        return
    middle = preorder[0]
    middle_idx = inorder.index(middle)
    
    left_in = inorder[:middle_idx]
    left_pre = preorder[1:middle_idx+1]
    if len(left_in)!=0:
        toPostorder(left_pre,left_in)
    
    right_in = inorder[middle_idx+1:]
    right_pre = preorder[middle_idx+1:]
    if len(right_in)!=0:
        toPostorder(right_pre,right_in)
    
    print(middle,end=" ")

t = int(input())

for _ in range(t):
    n = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    
    toPostorder(preorder,inorder)
    print()