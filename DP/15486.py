# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 22:10:44 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

n = int(input())
time=[0]*(n+1)
pay=[0]*(n+1)

for i in range(n):
    t,p = map(int,input().split())
    time[i]=t
    pay[i]=p

#dp배열
dp=[0]*(n+1)

max_val=0
for i in range(n,-1,-1):
    if i+time[i]<=n:
        dp[i]=max(max_val,pay[i]+dp[i+time[i]])
        max_val = dp[i]
    else:
        dp[i]=max_val
print(max_val)
        