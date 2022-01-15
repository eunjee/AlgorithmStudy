# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:10:06 2021

@author: 조은지
"""
n = int(input())

RGB=[] #RGB비용

for i in range(n):
    line = list(map(int,input().split()))
    RGB.append(line)

for i in range(1,n):
    #i번째에 빨간색을 칠하는 경우
    RGB[i][0] = min(RGB[i-1][1],RGB[i-1][2])+RGB[i][0]
    #i번째에 초록색을 칠하는 경우
    RGB[i][1] = min(RGB[i-1][0],RGB[i-1][2])+RGB[i][1]
    #i번째에 파란색을 칠하는 경우
    RGB[i][2] = min(RGB[i-1][0],RGB[i-1][1])+RGB[i][2]

print(min(RGB[n-1]))
