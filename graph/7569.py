#토마토 22-02-05
import sys
from collections import deque
input = sys.stdin.readline
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

m,n,h = map(int,input().split()) #가로,세로,높이
graph=[]
q= deque([])
for i in range(h):
    tmp=[]
    for j in range(n):
        tmp.append(list(map(int,input().split())))
        for k in range(m): #토마토 위치 미리 넣어두기
            if tmp[j][k]==1:
                q.append([i,j,k]) #높이,세로,가로
    graph.append(tmp) #한 층 입력 받기


while q:
    x,y,z =q.popleft()
    for i in range(6):
        nx=x+dx[i]
        ny=y+dy[i]
        nz=z+dz[i]
        if 0<=nx<h and 0<=ny<n and 0<=nz<m:
            if graph[nx][ny][nz]==0:
                q.append([nx,ny,nz])
                graph[nx][ny][nz]=graph[x][y][z]+1
days=0
for layer in graph:
    for line in layer:
        for k in line:
            if k==0:
                print(-1)
                exit(0)
        days=max(days,max(line))
print(days-1)