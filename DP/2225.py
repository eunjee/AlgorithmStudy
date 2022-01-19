# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 23:15:34 2022

@author: 조은지
"""
import sys
#input = sys.stdin.readline

n,k = map(int,input().split())
dp=[[0]*201 for i in range(201)]

#k=1일 때, k=2일 때
for i in range(n+1):
    dp[1][i]=1
    dp[2][i]=i+1
    
#k=3부터
for t in range(3,k+1):
    dp[t][0]=1
    for i in range(1,n+1):
        dp[t][i]=(dp[t-1][i]+dp[t][i-1])%1000000000

print(dp[k][n])