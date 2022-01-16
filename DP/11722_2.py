# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 02:25:42 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

n = int(input())
arr=list(map(int,input().split()))
arr.reverse()
dp=[1]*1001

#dp 
for i in range(1,n):
    for j in range(0,i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
    
    