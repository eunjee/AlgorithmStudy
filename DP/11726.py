# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 01:20:19 2022

@author: 조은지
"""
#2*n타일링
import sys
input = sys.stdin.readline

n = int(input())

dp=[0]*(1001)

if n>3:
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]= dp[i-1]+dp[i-2]
    print(dp[-1]%10007)
else:
    print(n)
        