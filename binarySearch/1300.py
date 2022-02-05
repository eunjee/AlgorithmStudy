# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:11:05 2021

@author: 조은지
"""
#가장 큰 수 - 시간초과 (이분탐색 사용 X)
n = int(input())
k = int(input())

B =[] #일차원 배열 B

for i in range(1,n+1):
    for j in range(1,n+1):
        B.append(i*j)

B.sort()

print(B[k-1])