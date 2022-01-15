import heapq

#무한대 값을 설정
INF = int(1e9)

#노드와 간선의 개수 입력 받기 
n,m,start = map(int,input().split())

#다익스트라를 위해 필요한 자료구조
graph=[[] for i in range(n+1)] #인접리스트
distance=[INF]*(n+1) #최단 거리 테이블

#모든 간선 정보 입력받기
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c]) #단방향 그래프, a->b까지의 거리가 c임을 저장한다. 

#다익스트라
def dijkstra(start):
    q=[]
    #출발노드 초기화
    distance[start]=0
    heapq.heappush(q,(0,start)) #distance, node
    
    while q:
        dist, node = heapq.heappop(q) #노드 선택
        if distance[node] < dist: #이미 방문했었던 노드라면 무시
            continue
        
        for i in graph[node]:
            cost = dist+i[1] #노드를 거쳐갔을 때의 비용
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    
dijkstra(start)
print(max(distance[1:]))