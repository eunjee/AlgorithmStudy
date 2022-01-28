#구간나누기2 22-01-28

n,m = map(int,input().split())
arr = list(map(int,input().split()))

answer=0

#구간 나누기 (실패 -> 최솟값과 최댓값을 보장하지 못합)
def divide(mid):
    s=e=cnt=0
    while e<n:
        if abs(arr[e]-arr[s])>=mid:
            cnt+=1
            s+=1
            e=s #다음 위치로 이동
        else:
            e+=1
    return cnt

start = 0 #최소
end=max(arr) #최대
#구간의 최댓값을 기준으로 이분탐색
while start<=end:
    mid = (start+end)//2
    print(mid,divide(mid))
    if divide(mid)>m: #구간의 수가 많다면?
        start=mid+1 #최댓값을 늘린다.
    else:
        end=mid-1 #최댓값을 줄인다
        answer=mid
print(answer)