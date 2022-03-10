
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n>1:
            dp=[[0,0] for _ in range(n+1)]
            dp[0]=[1,0]
            dp[1]=[0,1]
            for i in range(2, n+1):
                dp[i][0] = dp[i-1][1]
                dp[i][1] = dp[i-1][0]+dp[i-1][1]
            print(*dp[n])
        elif n==1:
            print(0,1)
        else:
            print(1,0)