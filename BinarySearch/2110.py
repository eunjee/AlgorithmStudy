# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:34:04 2021

@author: 조은지
"""

def binary_search(start,end):
    result =0
    while start<=end:
        mid = (start+end)//2
        current = arr[0]
        count=1
        for  i in range(1,len(arr)):
            if arr[i]>=current+mid:
                count+=1
                current=arr[i] #i번째에 공유기 설치
        if count>=c:
            result = mid
            start = mid+1 #거리를 더 멀리 둔다.
        else:
            end = mid-1 #거리를 더 좁게 둔다. 
    return result

n,c = map(int,input().split())
arr=[]

for i in range(n):
    tmp = int(input())
    arr.append(tmp)
    
arr.sort()

print(binary_search(1, arr[-1]-arr[0]))