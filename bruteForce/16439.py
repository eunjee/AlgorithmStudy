# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 00:04:54 2022

@author: 조은지
"""
from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

prefer = [list(map(int,input().split()))for _ in range(n)]
idx=[i for i in range(m)]

res=0
it = combinations(idx, 3)
for i in it:
    tmp=0
    for j in range(n):
        tmp+=max(prefer[j][i[0]],prefer[j][i[1]],prefer[j][i[2]])
    res = max(res,tmp)

print(res)
