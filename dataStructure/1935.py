# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 09:16:57 2021

@author: 조은지
"""
import sys
from collections import deque
input = sys.stdin.readline


n = int(input())

notation = input().rstrip()
stack=[]
nums = [int(input()) for _ in range(n)]
for no in notation:
    if no.isalpha():
        stack.append(nums[ord(no)-ord('A')])
    else:
        if no =='*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        elif no =='+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif no =='-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif no =='/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
        
print(format(stack[0],".2f"))  
    