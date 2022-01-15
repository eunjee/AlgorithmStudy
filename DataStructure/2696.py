# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:30:32 2022

@author: 조은지
"""
import heapq
import sys

input = sys.stdin.readline

def solution(arr):
    left=[]
    right=[]
    middle = arr[0]
    result = [middle]
    
    for idx,val in enumerate(arr[1:],1):
        if val>middle:
            heapq.heappush(right, val)
        else:
            heapq.heappush(left,(-val,val))
        
        if idx%2==0:
            if len(left)<len(right):
                heapq.heappush(left,(-middle,middle))
                middle = heapq.heappop(right)
            elif len(left)>len(right):
                heapq.heappush(right,middle)
                middle = heapq.heappop(left)[1]
            result.append(middle)
    #출력
    print(len(result))
    for i in range(len(result)):
        if i!=0 and (i+1)%10==1:
            print()
        print(result[i],end=" ")
    print()

t = int(input())    
for _ in range(t):
    m = int(input())
    arr=[]
    if m%10==0:
        for i in range(m//10):
            arr.extend(list(map(int,input().rstrip().split())))
    else:
        for i in range(m//10+1):
            arr.extend(list(map(int,input().rstrip().split())))
    
    solution(arr)
    