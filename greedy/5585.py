# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:22:02 2021

@author: 조은지
"""
import sys

input = sys.stdin.readline

n = 1000- int(input())

#500,100,50,10,5

count = 0
money=[500,100,50,10,5,1]
for m in money:
    count += n//m
    n%=m

print(count)