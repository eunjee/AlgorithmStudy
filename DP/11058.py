#크리보드
if __name__ == '__main__':
    n = int(input())
    dp=[0]*101
    if n<4:
        print(n)
    else:
        #초기화
        for i in range(1,7):
            dp[i]=i
        #dp
        for i in range(7,n+1):
            dp[i] = max(i,dp[i-3]*2,dp[i-4]*3,dp[i-5]*4)
        print(dp[n])