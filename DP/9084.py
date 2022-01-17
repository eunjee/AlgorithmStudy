# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 23:50:49 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

t= int(input())
for _ in range(t):
    n = int(input()) #동전의 가지 수
    coin = list(map(int,input().split())) #동전 단위
    m = int(input()) #금액
    dp=[0]*(m+1)
    dp[0]=1
    #dp - 금액을 만드는 모든 방법
    for c in coin:
        for i in range(1,m+1):
            if i>=c:
                dp[i]+=dp[i-c]
    print(dp[m])