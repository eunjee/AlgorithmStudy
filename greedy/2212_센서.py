# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 21:57:44 2022

@author: 조은지
"""
import sys
input= sys.stdin.readline
n = int(input())
k = int(input())

if n<=k:
    print(0)
    sys.exit(0)
    
sensor = list(map(int,input().split()))
sensor.sort() #위치를 오름차순으로 정렬

distance=[] #센서 사이의 거리
for i in range(1,n):
    distance.append(sensor[i]-sensor[i-1])

distance.sort(reverse=True)

for i in range(k-1):
    distance.pop(0)

print(sum(distance))