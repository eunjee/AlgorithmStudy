# 14940번 쉬운최단거리 (틀린 코드)  21-01-27
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j,1)) #위치,dist
    visited[i][j]=True #방문표시하기

    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny]!=0:
                    visited[nx][ny]=True
                    graph[nx][ny]=dist
                    q.append((nx,ny,dist+1))



n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)] #입력받기

visited=[[False]*m for _ in range(n)]

#목표지점 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            bfs(i,j)
            graph[i][j]=0
            break

for x in range(n):
    for y in range(m):
        if not visited[x][y] and graph[x][y] == 1:
            graph[x][y] = -1

for line in graph:
    print(*line)

