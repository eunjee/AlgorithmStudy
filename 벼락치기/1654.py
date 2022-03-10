import sys
input = sys.stdin.readline

if __name__ == '__main__':
    k,n = map(int,input().split())
    data = [int(input()) for _ in range(k)]
    answer = 0
    start=1
    end=max(data)
    while start<=end:
        mid = (start+end)//2
        count=0
        #랜선 개수 세기
        for d in data:
            count+=d//mid
        if count>=n: #길이 늘려
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)