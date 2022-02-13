#마법사 상어와 비바라기 22-02-13
import sys
from collections import deque
input = sys.stdin.readline

dx=[0,0,-1,-1,-1,0,1,1,1] #8방향 (인덱스 1부터 시작)
dy=[0,-1,-1,0,1,1,1,0,-1]

#구름이 있었던 칸을 제외한 나머지 칸에서 물의 양이 2 이상인 칸에 구름
def make_cloud():
    for i in range(n):
        for j in range(n):
            if graph[i][j]>=2 and not visited[i][j]:
                clouds.append((i,j))
                graph[i][j]-=2

#대각선 방향으로 체크 (2,4,6,8번)
#주의! 이 때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
def water_copy():
    while clouds:
        count=0
        x,y = clouds.popleft()
        for i in range(2,9,2):
            nx = (x+dx[i])
            ny = (y+dy[i])
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=0:
               count+=1
        graph[x][y]+=count #물이 있는 바구니 수만큼 물의 양 증가
    make_cloud()


#구름 이동 d방향으로 s만큼
def move_cloud(d,s):
    #구름 이동 후에 비내리기
    length=len(clouds)
    for _ in range(length):
        x,y = clouds.popleft()
        nx=(x+dx[d]*s)%n #행,열이 연결되어있음
        ny=(y+dy[d]*s)%n
        if nx<0:
            nx+=n
        if ny<0:
            ny+=n
        clouds.append((nx,ny))
        graph[nx][ny]+=1
        visited[nx][ny]=True #구름 이동 표시

    water_copy() #물 복사하기


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = []
clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]  # 초기 구름
clouds=deque(clouds)
for _ in range(m):
    visited=[[False]*n for _ in range(n)] #구름 표시
    d,s=map(int,input().split())
    move_cloud(d,s)

answer=0
#구름 이동
for i in range(n):
    answer+=sum(graph[i])
print(answer)

