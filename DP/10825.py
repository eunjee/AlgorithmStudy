# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:20:54 2021

@author: 조은지
"""
import sys

input = sys.stdin.readline
#모든 값에 대해 정렬하기 쉽게 리스트를 생성함
students =[]
n = int(input())

for _ in range(n):
    line = list(input().split())
    for i in range(1,4):
        line[i]=int(line[i])
    students.append(line)
    

#이름을 사전순으로 정렬(오름차순)
students.sort()

#수학점수 내림차순으로 정렬
students.sort(key = lambda x:x[3],reverse=True)

#영어점수 오름차순으로 정렬
students.sort(key = lambda x:x[2])

#국어점수 내림차순으로 정렬
students.sort(key = lambda x:x[1],reverse=True)

for i in range(n):
    print(students[i][0])
