# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:52:42 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

n = int(input())
mod = 1000000000

dp=[[0]*10 for i in range(n+1)]

dp[1]=[0,1,1,1,1,1,1,1,1,1]

for i in range(2,n+1):
    #끝자리가 0인 경우
    dp[i][0]=dp[i-1][1]
    #끝자리가 9인 경우
    dp[i][9]=dp[i-1][8]
    
    #나머지
    for j in range(1,9):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]

print(sum(dp[n])%1000000000)
    
