# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:53:12 2021

@author: 조은지
"""
n = int(input())

s= list(map(int,input().split()))

lis=[0]*n

lis[0]=1
for i in range(1,n):
   for j in range(i):
       if s[j]<s[i] and lis[j]>lis[i]:
           lis[i] = lis[j]
   lis[i]+=1

print(max(lis))    
