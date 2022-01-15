# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 21:02:10 2022

@author: 조은지
"""
import sys
t = int(input())
for _ in range(t):
    n,m = map(int,input().split()) #세로 가로
    arr=list(map(int,input().split()))
        
    #2차원 테이블로 바꾸기
    dp=[]
    idx=0
    for i in range(n):
        dp.append(arr[idx:idx+m])
        idx+=m

    #dp, i열에서 최댓값을 결정하는 방식
    for j in range(1,m):
        for i in range(n):
            #왼쪽 아래 혹은 왼쪽만 가능
            if i==0:
                dp[i][j] += max(dp[i][j-1],dp[i+1][j-1])
                #왼쪽 위 혹은 왼쪽만 가능
            elif i==n-1:
                dp[i][j] +=max(dp[i-1][j-1],dp[i][j-1])
            else:
                dp[i][j]+=max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])
                        
    ans=0
    for i in range(n):
        ans=max(ans,dp[i][m-1]) 
    print(ans)          
