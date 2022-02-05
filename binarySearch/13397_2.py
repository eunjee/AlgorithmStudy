#구간나누기2 22-01-28
n,m=map(int,input().strip().split())
arr=list(map(int,input().strip().split()))
#투포인터
def divide(x):
    max_x=min_x=arr[0]
    cnt=1
    for i in range(1,n):
        max_x=max(max_x,arr[i])
        min_x=min(min_x,arr[i])
        if max_x - min_x > x:
            cnt+=1
            max_x=arr[i]
            min_x=arr[i]
    return cnt

start, end = 0, max(arr)
result=0
while start<=end:
    mid=(start+end)//2
    if divide(mid)<=m:
        end = mid-1
        result=mid
    else:
        start = mid+1

print(result)
