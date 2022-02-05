# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:11:38 2021

@author: 조은지
"""
import sys
input = sys.stdin.readline
n = int(input())
arr=[]

for _ in range(n):
    w = input().split()
    if w[0]=="push":
        arr.append(int(w[1]))
    if w[0]== "pop":
        if len(arr)>0:
            print(arr[-1])
            del arr[-1]
        else:
            print(-1)
    if w[0]=="top":
        if len(arr)>0:
            print(arr[-1])
        else:
            print(-1)
    if w[0]=="size":
        print(len(arr))
    if w[0]=="empty":
        if len(arr)==0:
            print(1)
        else:
            print(0)
    