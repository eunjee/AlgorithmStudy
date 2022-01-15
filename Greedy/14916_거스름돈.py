# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:26:17 2021

@author: 조은지
"""
n = int(input())
if n in (1,3):
    print(-1)
   
elif (n%5)%2==0:
    print((n//5)+(n%5)//2)
    
else:
    tmp = n//5-1
    n-=tmp*5
    print(tmp+(n//2))
    