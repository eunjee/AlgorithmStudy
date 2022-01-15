# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:27:39 2021

@author: 조은지
"""
sentence = input()
removdot = sentence.replace('.',' ').split()
poly=['AAAA','BB']
def solution(removdot):
    answer=''
    #X길이가 홀수면 -1 리턴
    for idx,s in enumerate(removdot):
        length = len(s)
        if length%2!=0:
            print(-1)
            return -1
        if len(s)==2:
            answer+=poly[1]     
        elif len(s)>=4:
            answer+=poly[0]*(length//4)
            length%=4
            answer+=poly[1]*(length//2)
    return answer

answer = solution(removdot)
if answer!=-1:
    i=0
    solve=''
    for s in sentence:
        if s=='.':
            solve+='.'
        else:
            solve+=answer[i]
            i+=1
    print(solve)


