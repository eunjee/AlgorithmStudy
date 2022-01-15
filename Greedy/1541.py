# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 18:19:00 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline

sentence = input().split('-')

num=[]
for s in sentence:
    tmp=0
    ex = s.split('+')
    for a in ex:
        tmp+=int(a)
    num.append(tmp)
    
ans=num[0]
for n in num[1:]:
    ans-=n
print(ans)