# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 16:34:16 2021

@author: 조은지
"""
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    
    if mm[a][b][c]!=0:
        return mm[a][b][c]

    if a < b < c:
        mm[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return mm[a][b][c]
    else:
        mm[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return mm[a][b][c]

mm =[[[0 for col in range(21)] for row in range(21)] for depth in range(21)]
while True:
    a,b,c = map(int,input().split())
    
    if a==b==c==-1:
        break
    
    print('w({0}, {1}, {2}) = {3}'.format(a, b, c, w(a,b,c)))
    
    
    
    