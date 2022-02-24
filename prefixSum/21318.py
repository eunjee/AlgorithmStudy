import sys
input = sys.stdin.readline
n= int(input())
score=list(map(int,input().split())) #악보의 난이도
dp=[0]*n
#실수하는 악보 개수
for i in range(1,n):
    if score[i-1]>score[i]:
        dp[i]=dp[i-1]+1
    else:
        dp[i]=dp[i-1]

q = int(input())
for _ in range(q):
    x,y = map(int,input().split())
    print(dp[y-1]-dp[x-1])