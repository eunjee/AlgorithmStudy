#녹색 옷 입은 애가 젤다지? (복습) 22-03-02
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
INF = int(1e9)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
count=1
def dijkstra():
    heap = []
    heappush(heap,(graph[0][0],0,0)) #시작 위치

    while heap:
        dist,x,y = heappop(heap) #거리 가장 짧은 좌표를 pop
        if x==n-1 and y==n-1:
            print("Problem {0}: {1}".format(count,dist))
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                cost = dist+graph[nx][ny] #(x,y)를 거쳐서 nx,ny로 가는 경우
                if distance[nx][ny]<dist: #이전에 왔던 노드면 무시
                    continue
                if cost<distance[nx][ny]:
                    distance[nx][ny]=cost
                    heappush(heap,(distance[nx][ny],nx,ny)) #최솟값 갱신한 경우는 heappush

while True:
    n = int(input())
    if n==0:
        break
    graph = [list(map(int,input().split())) for _ in range(n)]
    distance = [[INF]*n for _ in range(n)] #2차원 거리 배열

    dijkstra()
    count+=1
