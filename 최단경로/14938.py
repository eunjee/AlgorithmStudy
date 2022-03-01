#서강그라운드 22-03-01
import sys
input = sys.stdin.readline
INF = int(1e9)

#지역의 수, 수색범위, 길의 개수
n,m,r = map(int,input().split())
items = [0]+list(map(int,input().split()))

graph = [[INF] * (n + 1) for i in range(n + 1)]  # 2차원 리스트를 만들고 모든 값을 INF로 초기화

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 간선과 비용 입력받기
for i in range(r):
    s, e, dist = map(int, input().split())
    graph[s][e] = dist
    graph[e][s] = dist


# 플로이드 워셜 실행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

total=[0]*(n+1)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            total[i]+=items[j]


print(max(total))