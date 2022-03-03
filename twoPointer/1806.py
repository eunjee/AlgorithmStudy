#부분합 22-03-03
import sys
input = sys.stdin.readline
INF = int(1e9)
def prefix_sum():
    answer = INF
    start = 0
    end = 1
    while start!=n:
        if prefix[end]-prefix[start]>=s:
            answer = min(answer,end-start)
            start+=1
        else:
            if end!=n:
                end+=1
            else:
                start+=1
    if answer==INF:
        print(0)
    else:
        print(answer)

n,s = map(int,input().split())
arr = list(map(int,input().split()))
prefix = [0]*(n+1)
for i in range(1,len(arr)+1):
    prefix[i]=prefix[i-1]+arr[i-1]

prefix_sum()