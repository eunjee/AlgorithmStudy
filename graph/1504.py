from heapq import heappush, heappop
import sys
INF = int(1e9)
input = sys.stdin.readline
def dijkstra(start):
    pq = []
    distance = [INF] * (n + 1)
    distance[start]=0
    heappush(pq,(0,start)) #distance,node

    while pq:
        dist,node = heappop(pq)
        if distance[node]<dist:
            continue
        for i in graph[node]:
            cost = dist+i[1] #노드를 거쳐갔을 때의 비용
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heappush(pq,(cost,i[0]))
    return distance

if __name__ == '__main__':
    n,e = map(int,input().split())
    graph=[[] for _ in range(n+1)]

    for _ in range(e):
        a,b,dist = map(int,input().split())
        graph[a].append((b,dist)) #a에서 b
        graph[b].append((a,dist)) #b에서 a
    v1,v2 = map(int,input().split()) #출발노드, 목표노드

    one = dijkstra(1)
    v1_ = dijkstra(v1)
    v2_ = dijkstra(v2)
    answer = min(one[v1]+v1_[v2]+v2_[n],one[v2]+v2_[v1]+v1_[n])
    if answer>=INF:
        print(-1)
    else:
        print(answer)
