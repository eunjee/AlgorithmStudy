#ATM 복습 22-03-07
if __name__=='__main__':
    n = int(input())
    times = list(map(int,input().split()))
    times.sort()
    arr = [0]*n
    arr[0]=times[0]
    for i in range(1,n):
        arr[i]=arr[i-1]+times[i]
    print(sum(arr))