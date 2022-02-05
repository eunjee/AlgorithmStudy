# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:38:24 2021

@author: 조은지
"""
import sys
#input = sys.stdin.readline

def cutting(mid):
    count=0
    for a in arr:
        count+= a//mid
    return count

def binary_search(start,end,target):
    result=0
    while start<=end:
        mid =(start+end)//2
        count = cutting(mid)
        if count<target:
            end = mid-1
        else:
            result = mid
            start = mid+1
    return result
            

n,k = map(int,input().split())

arr = []
for i in range(n):
    tmp = int(input())
    arr.append(tmp)
    
end= max(arr)
print(binary_search(1,end,k))