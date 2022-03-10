#평범한 배낭 복습 22-03-08
if __name__ == '__main__':
    n,k = map(int,input().split())
    data=[[0,0]]
    #처음부터 i번째까지의 물건을 살펴보고, 배낭의 용량이 j였을 때 배낭에 들어간 물건의 가치합의 최댓값
    dp= [[0]*(k+1) for _ in range(n+1)]
    for _ in range(n):
        data.append(list(map(int,input().split())))
    for i in range(1,n+1):
        for j in range(1,k+1):
            v = data[i][0]
            w = data[i][j]
            if j<w:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-v]+w)
    print(dp[n][k])