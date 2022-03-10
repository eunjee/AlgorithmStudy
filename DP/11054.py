import sys
input = sys.stdin.readline
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    #가장 증가하는 수열
    dp1=[1]*n
    for i in range(n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp1[i]=max(dp1[i],dp1[j]+1)
    #가장 감소하는 수열
    arr.reverse()
    dp2 =[1]*n
    for i in range(n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp2[i]=max(dp2[i],dp2[j]+1)
    dp2.reverse()
    max_val=0
    for i in range(n):
        max_val=max(max_val,dp1[i]+dp2[i])
    print(max_val-1)