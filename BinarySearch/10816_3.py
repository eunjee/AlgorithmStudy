# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:16:08 2021

@author: 조은지
"""
#bisect 구현
import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline

def lower_bound(target):
    start = 0
    end = n-1
    while start<=end:
        mid=(start+end)//2
        if target>cards[mid]:
            start = mid+1
        else:
            end = mid-1
    return start

def upper_bound(target):
    start = 0
    end = n-1
    while start<=end:
        mid =(start+end)//2
        if target>=cards[mid]:
            start = mid+1
        else:
            end = mid-1
    return start
n = int(input())

cards = list(map(int, input().split()))

m = int(input())

sg = list(map(int,input().split()))

cards.sort()

for s in sg:
    print(upper_bound(s)-lower_bound(s),end=' ')