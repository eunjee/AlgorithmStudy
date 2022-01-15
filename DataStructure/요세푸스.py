# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 21:55:00 2021

@author: 조은지
"""
import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

person = deque(i for i in range(1,n+1))
answer = []

for i in range(n):
    person.rotate(-k+1)
    p = person.popleft()
    answer.append(str(p))

print("<"+", ".join(answer)[:]+">")
    
    