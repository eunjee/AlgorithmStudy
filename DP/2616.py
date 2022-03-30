#소형기관차

if __name__ == '__main__':
    n = int(input())
    trains = list(map(int,input().split()))
    limit = int(input())

    #구간합
    S=[0]
    value=0
    for t in trains:
        value+=t
        S.append(value)

    #dp[i][j] = i번째 기차가 j번째 객차를 선택했을 때
    dp=[[0]*(n+1) for _ in range(4)]

    for i in range(1,4):
        for j in range(i*limit,n+1):
            if i==1:
                dp[i][j]=max(dp[i][j-1],S[j]-S[j-limit])
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j-limit]+S[j]-S[j-limit])

    print(dp[3][n])