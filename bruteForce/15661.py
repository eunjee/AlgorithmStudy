import sys
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
minv=1e9
def dfs(t,d,k):
    global minv
    if d==n:
        return
    if t==k:
        start=link=0
        for i in range(n):
            for j in range(n):
                if team[i]==True and team[j]==True:
                    start+=board[i][j]
                elif team[i]==False and team[j]==False:
                    link+=board[i][j]
        minv=min(abs(start-link),minv)
    else:
        team[d]=True
        dfs(t+1,d+1,k)
        team[d]=False
        dfs(t,d+1,k)
for k in range(1,int(n//2)+2): #주의할 부분 
    team = [False] * (n + 1)
    dfs(0,0,k)
print(minv)