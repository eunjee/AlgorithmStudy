# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:53:15 2021

@author: 조은지
"""
import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline


n = int(input())

cards = list(map(int, input().split()))

m = int(input())

sg = list(map(int,input().split()))

cards.sort()

for s in sg:
    print(bisect_right(cards,s)-bisect_left(cards,s),end=' ')