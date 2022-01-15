# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:15:19 2021

@author: 조은지
"""
n = int(input())

dp=[0]*(n+1)
dp[1]=1
dp[2]=2

for i in range(3,n+1):
    dp[i] =(dp[i-1]+dp[i-2])%10007
    
print(dp[n])