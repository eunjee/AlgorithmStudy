#안전영역 22-02-04
import sys
from collections import deque
input = sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(i,j,h):
    q = deque()
    q.append((i,j))
    visited[i][j]=True
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]>h and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny]=True


n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)] #입력받기

max_rain=0
for i in range(n):
    max_rain = max(max_rain,max(graph[i]))

answer=0
for i in range(0,max_rain+1):
    count=0
    visited=[[False]*n for _ in range(n)]
    #개수 세기
    for x in range(n):
        for y in range(n):
            if graph[x][y]>i and not visited[x][y]:
                bfs(x,y,i)
                count+=1
    answer=max(count,answer)

print(answer)
