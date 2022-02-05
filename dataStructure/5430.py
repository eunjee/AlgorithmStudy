# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 17:58:28 2021

@author: 조은지
"""
import sys
input = sys.stdin.readline
from collections import deque
t = int(input())

for _ in range(t):
    #조건들 입력
    ac = input().rstrip()
    n = int(input())
    s= input().rstrip()
    isError=False
    
    if n!=0:
        li = deque(s[1:-1].split(","))
    else:
        li = deque()
        
    rev=0
    for i in range(len(ac)):
        if ac[i]=="R":
            rev+=1
        else:
            if len(li)<1:
                isError=True
                print("error")
                break
            else:
                if rev%2==0: #앞에거 뺀다
                    li.popleft()
                else:
                    li.pop()
    if isError is False:
        if rev%2==1:
            li.reverse()
            print('['+','.join(li)+']')
        else:
            print('['+','.join(li)+']')