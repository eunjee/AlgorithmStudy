import sys
input = sys.stdin.readline
INF = int(1e9)
sys.setrecursionlimit(10**6)
dp=[]
def go(num,rem):
    global dp
    if num>=n:
        return 0
    elif dp[num][rem]!=INF:
        return dp[num][rem]
    else:
        #다음 줄에 작성하기
        next_rem = m-arr[num]
        dp[num][rem] = rem*rem + go((num+1),next_rem)

        #현재 줄에 작성할 수 있는 경우, 최솟값 찾기
        if arr[num]<rem and rem>0:
            next_rem = rem-arr[num]-1
            dp[num][rem] = min(dp[num][rem], go((num+1),next_rem))
    return dp[num][rem]
        

if __name__ == '__main__':
    n,m = map(int,input().split()) #세로, 가로
    arr = [int(input()) for _ in range(n)] #이름 길이

    dp=[[INF]*(m+1) for _ in range(n)]

    answer = go(1,m-arr[0])
    print(answer)