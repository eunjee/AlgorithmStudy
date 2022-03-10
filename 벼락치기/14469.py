import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    times=[]
    for _ in range(n):
        a,b = map(int, input().strip().split())
        times.append([a,b])
    times.sort(key=lambda x:x[0]) #도착시간을 기준으로 오름차순
    result=times[0][0]+times[0][1]
    for i in range(1,n):
        if times[i][0]>=result:
            result=times[i][0]+times[i][1]
        else:
            result+=times[i][1]
    print(result)