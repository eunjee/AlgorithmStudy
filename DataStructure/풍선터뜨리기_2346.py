# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:44:29 2021

@author: 조은지
"""
import sys
from collections import deque
input = sys.stdin.readline

#입력받기
n = int(input())
nums = list(map(int,input().split()))

answer=[]
#큐에 담기
q = deque()
for i in range(n):
    q.append([i+1,nums[i]])

#첫번째 빼기
idx,num = q.popleft()
answer.append(idx)

while q:
    if num>0:
        num-=1
    q.rotate(-num)
    idx,num = q.popleft()
    answer.append(idx)

for a in answer:
    print(a,end=" ")