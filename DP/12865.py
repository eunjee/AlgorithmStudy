# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:12:11 2021

@author: 조은지
"""
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

laguage = [[0,0]]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    laguage.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = laguage[i][0]
        v = laguage[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])
             