# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:37:37 2021

@author: 조은지
"""
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

#LIS사용
arr.reverse()
dp = [1]*n
for i in range(1,n):
    for j in range(0,i):
        if arr[j]<arr[i]:
            dp[i] = max(dp[i],dp[j]+1)


print(n-max(dp))