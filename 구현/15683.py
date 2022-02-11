#감시 22-02-11
from collections import deque
import sys
input = sys.stdin.readline
dx=[-1,1,0,0] #상하좌우
dy=[0,0,-1,1]
#cctv번호 별 탐색방향
directions=[[],
            [[0],[1],[2],[3]],
            [[0,1],[2,3]],
            [[0,3],[1,3],[1,2],[0,2]],
            [[0,2,3],[1,2,3],[0,1,2],[0,1,3]],
            [[0,1,2,3]]]

answer=int(1e9)
#cctv 완전탐색 (재귀로 cctv 완전탐색을 실행한다.)
def counting_zero():
    count=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                count+=1
    return count

def monitoring(index):
    global answer;
    if index==cctv_num:
        answer = min(answer,counting_zero())
        return

    sx,sy,number = cctv[index][0],cctv[index][1],cctv[index][2]
    direction=directions[number] #cctv 번호 선택

    for d in direction: #탐색 가능한 방향 리스트
        q = deque()
        for i in d: #한 방향 탐색
            x = sx
            y = sy
            while True:
                x+=dx[i]
                y+=dy[i]
                if 0<=x<n and 0<=y<m: #범위 내에 들고
                    if graph[x][y]==0: #0이면 탐색
                        graph[x][y]='#'
                        q.append((x,y))
                    elif graph[x][y]==6:#벽이면 탐색 중지
                        break
                else:
                    break
        monitoring(index+1)
        while q:
            x, y = q.popleft()
            graph[x][y] = 0  # 원상복귀




n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cctv=[]
#cctv 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j]!=0 and graph[i][j]!=6:
            cctv.append((i,j,graph[i][j])) #cctv위치, cctv번호

cctv_num=len(cctv) #cctv 개수
monitoring(0)
print(answer)