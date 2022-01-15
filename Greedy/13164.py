# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 23:39:54 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
person = list(map(int, input().split()))

diff = []
for i in range(N-1):
    diff.append(person[i+1] - person[i])
diff.sort()

answer = 0
for i in range(N-K):
    answer += diff[i]
print(answer)