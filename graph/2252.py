#줄세우기
from collections import deque
def topology():
    result=[]
    q = deque()

    #진입차수 0인 노드 삽입
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    #큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    print(*result)

if __name__ == '__main__':
    n,m = map(int,input().split())
    indegree=[0]*(n+1) #진입차수
    graph=[[] for i in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b) #a가 b앞에 있어야 한다.
        indegree[b]+=1
    topology()