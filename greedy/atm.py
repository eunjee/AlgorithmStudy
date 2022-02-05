# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 17:19:48 2022

@author: 조은지
"""
n = int(input())
time = list(map(int,input().split()))
total=[0]*n

#시간을 오름차순으로 정렬
time.sort()
total[0]=time[0]
for i in range(1,n):
    total[i]=time[i]+total[i-1]

print(sum(total))    
        
    