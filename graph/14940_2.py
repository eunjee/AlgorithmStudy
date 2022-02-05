# 쉬운 최단거리 성공코드
import sys
input = sys.stdin.readline
from collections import deque

def BFS(i,j):
    global dp_dists
    queue = deque()
    queue.append([i,j])
    dp_dists[i][j] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and dp_dists[nx][ny] == -1 :
                queue.append([nx,ny])
                dp_dists[nx][ny] = dp_dists[x][y]+1

def find_start():
    for i in range(n):
        for j in range(m):
            if not maps[i][j]:
                dp_dists[i][j]=0
    for i in range(n):
        for j in range(m):
            if maps[i][j]==2:
                BFS(i,j)
                return

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dp_dists = [[-1 for _ in range(m)] for _ in range(n)] #방문표시 and 거리 저장하는 리스트
dx = [0,1,-1,0]
dy = [1,0,0,-1]

find_start()

for i in range(n):
    print(*dp_dists[i])