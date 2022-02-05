# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 15:05:19 2021

@author: 조은지
"""
import sys
input = sys.stdin.readline
import heapq

#최소힙, 최대힙
min_h = []
max_h = []
flag = dict()

#입력받기
n = int(input())
for i in range(n):
    p,l = map(int,input().split())
    heapq.heappush(min_h,(l,p))
    heapq.heappush(max_h, (-l,p))
    flag[p]=True

#명령어 입력
m = int(input())
for i in range(m):
    comm = input().split()
    if comm[0]=='recommend':
        if comm[1]=='1':
            while not flag[max_h[0][1]]:
                heapq.heappop(max_h)
            print(max_h[0][1])
        else:
            while not flag[min_h[0][1]]:
                heapq.heappop(min_h)
            print(min_h[0][1])            
            
    elif comm[0]=='solved':
        flag[int(comm[1])]=False
        
    else: 
        p = int(comm[1])
        l = int(comm[2])
        while not flag[min_h[0][1]]:
            heapq.heappop(min_h)
        while not flag[max_h[0][1]]:
            heapq.heappop(max_h)
        flag[p] = True
        heapq.heappush(min_h, (l,p))
        heapq.heappush(max_h,(-l,p))

            