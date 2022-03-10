import sys
from collections import deque
input = sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque()
    q.append((0,0,0)) #위치, dist

    while q:
        x,y,dist = q.popleft()
        if x==n-1 and y==m-1:
            return dist+1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]=='1':
                    graph[nx][ny]='0'
                    q.append((nx,ny,dist+1))
    return

if __name__ == '__main__':
    n,m = map(int,input().split())
    graph=[list(input().strip()) for _ in range(n)]
    print(bfs())