# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:02:35 2021

@author: 조은지
"""
#숫자카드2
import sys
input = sys.stdin.readline

def count_card(mid,target):
    count=1
    if cards[mid-1]==target:
        for i in range(mid-1,-1,-1):
            if cards[i]!=target:
                break
            count+=1
    if cards[mid+1]==target:
        for i in range(mid+1,n):
            if cards[i]!=target:
                break
            count+=1
    return count

def binary_search(start,end,target):
    while start<=end:
        mid = (start+end)//2
        if cards[mid]==target:
            if mid==0 or mid==n-1:
                return 1
            else:
                return count_card(mid,target)
        elif cards[mid]>target:
            end = mid-1
        else:
            start = mid+1
    
    return 0
    

n = int(input())

cards = list(map(int, input().split()))

m = int(input())

sg = list(map(int,input().split()))

cards.sort() #오름차순으로 정렬


for s in sg:
    print(binary_search(0,n-1,s),end=' ')