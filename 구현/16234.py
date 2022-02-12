import sys
from collections import deque
input = sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,l,r = map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

#출력: 인구이동이 며칠동안 발생하는지
def bfs(i,j):
    global flag
    q=deque()
    q.append((i,j))
    visited[i][j]=True
    union=[]
    union.append((i,j)) #연합인 국가들
    total=graph[i][j]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if l<=abs(graph[x][y]-graph[nx][ny])<=r:
                    q.append((nx,ny)) #탐색할 큐에 넣기
                    union.append((nx,ny)) #연합인 국가에 넣기
                    total+=graph[nx][ny] #총 인구 수
                    visited[nx][ny]=True

    move=total//len(union) #인구 이동
    for x,y in union:
        graph[x][y]=move

    if len(union)>1:
        flag=True
    return



answer=0
while True:
    visited=[[False]*n for _ in range(n)] #방문
    flag=False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j)
    if flag:
        answer+=1
    else:
        print(answer)
        break