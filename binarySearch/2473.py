#세 용액 22-02-06 완전탐색
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
solutions = list(map(int,input().split()))

comb = combinations(solutions,3)

answer=int(1e9)
answerList = []
for c in comb:
    if answer>abs(sum(c)):
        answerList = list(c)
        answer=abs(sum(c))
        if answer==0:
            break
answerList.sort()
print(*answerList)
