#아기상어 22-02-10
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n = int(input())
space=[list(map(int,input().split())) for _ in range(n)]

sx,sy=0,0
answer=0 #이동 시간
#아기 상어 위치 찾기
for i in range(n):
    if 9 in space[i]:
        sx=i
        sy=space[i].index(9)
        space[sx][sy]=0
        break

size=2
eat=0
#다른 물고기 위치 확인 BFS
while True:
    q= deque()
    q.append((sx,sy,0)) #시작위치
    visited=[[False]*n for _ in range(n)]
    fish=[]
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and space[nx][ny]<=size:
                    if space[nx][ny]!=0 and space[nx][ny]<size:
                        fish.append((nx,ny,dist+1))
                    visited[nx][ny]=True
                    q.append((nx,ny,dist+1))
    if not fish:
        break
    else: #거리로 정렬 -> x로 정렬, y로 정렬
        fish.sort(key=lambda x:(x[2],x[0],x[1]))
        answer+=fish[0][2]
        x,y = fish[0][0],fish[0][1]
        space[x][y]=0 #먹힘
        eat+=1
        if eat==size:
            size+=1
            eat=0
        sx,sy=x,y #상어의 위치 이동


print(answer)


