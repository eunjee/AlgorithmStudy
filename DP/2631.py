#줄세우기 22-03-09
if __name__ == '__main__':
    n = int(input())
    children =[int(input()) for _ in range(n)]
    dp=[1]*(n+1)
    for i in range(n):
        for j in range(i):
            if children[i]>children[j]:
                dp[i]=max(dp[i],dp[j]+1)
    print(n-max(dp))