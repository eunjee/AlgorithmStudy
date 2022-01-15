# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 22:58:17 2021

@author: 조은지
"""
n = int(input())
s=[]
for i in range(n):
    s.append(int(input()))

dp=[0]*n

if n>=3:
    dp[0] = s[0]
    dp[1] = s[0]+s[1]
    dp[2] = max(s[1]+s[2],s[0]+s[2])
    if n>3:
        for i in range(3,n):
            dp[i] = max(dp[i-3]+s[i-1],dp[i-2])+s[i]
    print(dp[-1])
    
else:
    print(sum(s))