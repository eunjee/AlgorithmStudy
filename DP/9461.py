# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 01:42:10 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp=[0]*101
    if n>3:
        dp[1]=1
        dp[2]=1
        dp[3]=1
        for i in range(4,n+1):
            dp[i]=dp[i-2]+dp[i-3]
        print(dp[n])
    else:
        print(1)