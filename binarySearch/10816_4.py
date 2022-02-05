# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:28:37 2021

@author: 조은지
"""
#숫자카드 - 딕셔너리
import sys
input = sys.stdin.readline

n = int(input())

cards = list(map(int, input().split()))

cards.sort()

count={}

for c in cards: #미리 카드의 개수를 센다
    if c in count:
        count[c]+=1
    else:
        count[c]=1
        
m = int(input())

sg = list(map(int,input().split()))

for s in sg:
    if s in count:
        print(count[s],end=' ')
    else:
        print(0, end=' ')

