#예산 22-01-29
import sys
input = sys.stdin.readline
#입력받기
n = int(input())
req = list(map(int,input().split()))
total = int(input())

start = 0
end = max(req) #분배하는 최대 예산
answer=0
while start<=end:
    mid = (start+end)//2
    tmp = total
    for r in req:
        if tmp>=0:
            if r<=mid:
                tmp-=r
            else:
                tmp-=mid
    if tmp>=0: #예산 늘려바
        start = mid+1
        answer = mid
    else: #예산 줄여
        end=mid-1
print(answer)