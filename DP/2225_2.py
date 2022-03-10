if __name__ == '__main__':
    n,k = map(int,input().split())
    dp=[[0]*201 for _ in range(201)]

    #k*n의 배열

    #k가 1혹은 2일 때
    for i in range(n+1):
        dp[1][i]=1
        dp[2][i]=i+1

    #k가 3이상일 때
    for i in range(3,k+1):
        dp[i][0]=1
        for j in range(1,n+1):
            dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000000000
    print(dp[k][n])

