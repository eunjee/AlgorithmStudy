import sys
from collections import deque
input = sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(i,j):
    q=deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for t in range(4):
            nx=x+dx[t]
            ny=y+dy[t]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1:
                    q.append((nx,ny))
                    graph[nx][ny]=0

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m,n,k = map(int,input().split())
        graph = [[0]*m for _ in range(n)]
        for kk in range(k):
            y,x = map(int,input().split())
            graph[x][y]=1
            count=0
        for i in range(n):
            for j in range(m):
                if graph[i][j]==1:
                    count+=1
                    bfs(i,j)
        print(count)
