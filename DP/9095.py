# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:34:05 2021

@author: 조은지
"""
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    dp=[0]*(n+1)
    
    dp[1]=1
    if n>=2:
        dp[2]=2
    if n>=3:
        dp[3]=4
    
    if n>3:
        for j in range(4,n+1):
            dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
    
    print(dp[-1])