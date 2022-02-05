# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:17:36 2021

@author: 조은지
"""
import sys
input = sys.stdin.readline

n = int(input())
a= list(map(int,input().split()))
b= list(map(int,input().split()))
a.sort(reverse=True)
b.sort()

answer=0

for i in range(n):
    answer+=a[i]*b[i]

print(answer)