#내리막길 22-03-15
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
INF = int(1e9)
dx=[-1,1,0,0]#상하좌우
dy=[0,0,-1,1]

def dfs(x,y):
    if x==n-1 and y==m-1: #도착하면 경로 개수 +1
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    dp[x][y]=0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny]<graph[x][y]: #graph[nx][ny]의 높이가 더 낮아야 한다.
                dp[x][y]+=dfs(nx,ny)
    return dp[x][y]

if __name__ == '__main__':
    n,m = map(int,input().split())
    graph=[list(map(int,input().split())) for _ in range(n)]
    dp = [[-1]*m for _ in range(n)] #dp 배열

    print(dfs(0,0))
