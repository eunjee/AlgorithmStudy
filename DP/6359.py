# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 00:14:48 2021

@author: 조은지
"""
t = int(input())

for _ in range(t):
    n = int(input())
    #처음에 모든 문을 열기 때문에 1로 설정
    dp = [1]*(n+1)
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            dp[j]= -dp[j]
    
    print(dp.count(1)-1)


            
        