# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 21:28:21 2022

@author: 조은지
"""
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

dp=[[0]*n for _ in range(n)]

dp[0][0]=1
for i in range(n):
    for j in range(n):
        dist=arr[i][j]
        if dist!=0:
            if i+dist<n:
                dp[i+dist][j] +=dp[i][j]
            if j+dist<n:
                dp[i][j+dist]+=dp[i][j]

print(dp[-1][-1])

