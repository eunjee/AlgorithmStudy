# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:40:44 2021

@author: 조은지
"""
from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    priority = list(map(int,input().split()))
    q1 = deque() #값을 넣음
    q2 = deque() #인덱스를 넣음
    for i in range(len(priority)):
        q1.append(priority[i])
        q2.append(i)
    count=1
    while True:
        #첫번째 애가 최대 
        if q1[0]==max(q1):
            if q2[0]==m: #얘가 답이면
                print(count)
                break
            else:
                q1.popleft() #아니면 걍 출력
                q2.popleft()
                count+=1
        else:
            q1.append(q1[0])
            q2.append(q2[0])
            q1.popleft()
            q2.popleft()