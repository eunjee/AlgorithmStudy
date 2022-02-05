# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 22:29:59 2021

@author: 조은지
"""
n = int(input())
arr=[]

for i in range(n):
    line = list(map(int,input().split()))
    arr.append(line)

arr.sort(key=lambda x:(x[1],x[0]))
end = arr[0][1]
count=1
for i in range(n):
    #start>=end
    if arr[i][0]>=end:
        end = arr[i][1]
        count+=1

print(count)