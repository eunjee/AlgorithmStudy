# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 16:34:38 2021

@author: 조은지
"""
import sys
input = sys.stdin.readline
sentence = list(input())
stack = []

res=''
for s in sentence:
    if s.isalpha(): #알파벳이면 문장에 넣기
        res+=s
    else:
        if s =='(':
            stack.append(s)
        elif s=='*'or s=='/':
            while stack and (stack[-1]=='*'or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(s)
        elif s=='+' or s=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(s)
        elif s==')':
            while stack and stack[-1]!="(":
                res+=stack.pop()
            stack.pop()

while stack:
    res+=stack.pop()
    
print(res)

        