# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 23:17:36 2021

@author: 조은지
"""

n = int(input())
arr = list(map(int,input().split()))

arr.sort()


for i in range(1,n):
    arr[i]+=arr[i-1]

print(sum(arr))