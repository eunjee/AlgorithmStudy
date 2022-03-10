#플로이드 [22-03-05]
import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input()) #도시 개수
m = int(input()) #버스 개수

graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1): #자기 자신으로 가는 비용은 0으로
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for i in range(m):
    a,b,c = map(int,input().split())
    if graph[a][b]>c:
        graph[a][b]=c

#플로이드 워셜 알고리즘
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
#출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()