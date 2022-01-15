# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:53:34 2021

@author: 조은지
"""
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [list(map(int,input().rstrip().split())) for i in range(2)]
    
    if n==1:
        print(max(sticker[0][0],sticker[1][0]))
        continue
    
    #dp
    sticker[0][1]+=sticker[1][0]
    sticker[1][1]+=sticker[0][0]
    if n>3:
        for j in range(2,n):
            #교차로 하거나 한칸 건너뛰거나
            sticker[0][j] += max(sticker[1][j-1],sticker[1][j-2])
            sticker[1][j] += max(sticker[0][j-1],sticker[0][j-2])

    print(max(sticker[0][n-1],sticker[1][n-1]))