# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 17:07:31 2021

@author: 조은지
"""
n = int(input())

dp = [0]*(n+1)

dp[1]=1
if n>1:
    dp[2]=2
if n>=3:
    for i in range(3,n+1):
        dp[i] = (dp[i-1]+dp[i-2])%15746
    

print(dp[n])