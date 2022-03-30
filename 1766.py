#문제집 (위상정렬)
from heapq import heappush,heappop
if __name__ == '__main__':
    n,m = map(int,input().split()) #문제의 수, 먼저 푸는 것이 좋은 정보
    indegree=[0]*(n+1)
    graph=[[] for _ in range(n+1)] #그래프

    for _ in range(m):
        a,b = map(int,input().split()) #a먼저 풀고 b
        graph[a].append(b)
        indegree[b]+=1

    result=[]
    q = []
    for i in range(1,n+1):
        if indegree[i]==0:
            heappush(q,i)

    while q:
        now = heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                heappush(q,i)

    print(*result)