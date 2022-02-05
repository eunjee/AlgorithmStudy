#불! 22-01-29
# 참조 - https://seongonion.tistory.com/87
from collections import deque
import sys

input = sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1] #상하좌우
#입력받기
r,c = map(int,input().split())
maze=[list(input()) for _ in range(r)]
#초기화
jq = deque()
fq = deque()
jvisited=[[0]*c for _ in range(r)]
fvisited=[[0]*c for _ in range(r)]

#bfs
def bfs():
    #불 먼저 퍼지고
    while fq:
        fx,fy = fq.popleft()
        for i in range(4):
            nx = fx+dx[i]
            ny = fy+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if not fvisited[nx][ny] and maze[nx][ny]!='#':
                    fvisited[nx][ny]=fvisited[fx][fy]+1
                    fq.append((nx,ny))
    #지훈 이동
    while jq:
        jx,jy = jq.popleft()
        for i in range(4):
            nx = jx+dx[i]
            ny = jy+dy[i]
            if 0<=nx<r and 0<=ny<c:
                if not jvisited[nx][ny] and maze[nx][ny]!='#':
                    if not fvisited[nx][ny] or jvisited[jx][jy]+1<fvisited[nx][ny]: #불이 퍼진 시간 보다 빠르다면, 불이 이동하지 않은 경우도 고려해야 한다.
                        jvisited[nx][ny]=jvisited[jx][jy]+1 #이동
                        jq.append((nx,ny))
            else:
                return jvisited[jx][jy] #탈출한 경우
    return "IMPOSSIBLE"

#지훈이의 출발 위치
def find_start():
    for i in range(r):
        for j in range(c):
            if maze[i][j]=='J':
                jq.append((i,j))
                jvisited[i][j]=1
            elif maze[i][j]=='F':
                fq.append((i,j))
                fvisited[i][j]=1
    return bfs()

print(find_start())
