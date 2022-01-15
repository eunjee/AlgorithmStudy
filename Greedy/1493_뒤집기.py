# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 23:37:16 2021

@author: 조은지
"""

s = input()

count0=0
count1=0

if s[0]=='1':
    count0+=1
else:
    count1+=1

for i in range(len(s)-1):
    #문자가 달라지면 count+=1
    if s[i]!=s[i+1]:
        if s[i+1]=='1':
            count0+=1
        else:
            count1+=1

print(min(count0,count1))