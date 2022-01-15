# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 21:30:25 2022

@author: 조은지
"""
import sys
input = sys.stdin.readline
woman, man, k = map(int,input().split())

team =min(man,woman//2)

man -= team
woman -= team*2

if man+woman<k:
    k-=man+woman
    if k%3==0:
        team-=k//3
    else:
        team-=k//3+1

print(team)