#수들의 합 22-03-02
import sys
input = sys.stdin.readline

def count_m():
    count=0
    start = 0
    end=0
    while start<=end:
        prefix_sum = sum(arr[start:end])
        if prefix_sum>=m or end==n:
            start+=1
            if prefix_sum==m:
                count+=1
        if prefix_sum<m:
            end = min(end+1,n) #한 칸 이동

    return count

if __name__=='__main__':
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    print(count_m())