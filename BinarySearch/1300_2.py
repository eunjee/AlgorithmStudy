# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 14:15:37 2021

@author: 조은지
"""
n = int(input())
k = int(input())

start = 1
end = (n+1)**2

result=0
while start <=end:
    mid = (start+end)//2
    count=0
    for i in range(1,n+1):
        if (mid//i)<=n:
            count+=(mid//i)
        else:
            count+=n
    if count>=k:
        result=mid
        end = mid-1
    else:
        start = mid+1

print(result)