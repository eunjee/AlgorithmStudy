# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:46:24 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

n = int(input())

dp=[0]*(n+1)

for i in range(2,n+1):
    #현재의 수에서 1을 빼는 경우
    dp[i] = dp[i-1]+1
    #3으로 나누어지는 경우
    if i%3==0:
        dp[i] = min(dp[i],dp[i//3]+1)
    #2로 나누어지는 경우
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    
print(dp[n])
    
