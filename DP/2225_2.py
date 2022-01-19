# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 23:40:07 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dp=[0]*(201)

if k==1:
    print(1)
    sys.exit()
    
#k=2일 때 
for i in range(n+1):
    dp[i]=i+1

#k=3부터
for t in range(3,k+1):
    for i in range(1,n+1):
        dp[i]=(dp[i]+dp[i-1])%1000000000

print(dp[n])