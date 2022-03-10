import sys
from collections import deque
input = sys.stdin.readline
def bfs(a,b):
    q=deque()
    q.append((a,0))#나, 촌수
    while q:
        curr,dist = q.popleft()
        if curr==b:
            return dist
        for i in familly[curr]:
            if not visited[i]:
                q.append((i,dist+1))
                visited[i]=True
    return -1
if __name__ == '__main__':
    n = int(input())
    a,b = map(int,input().split())
    m = int(input())

    familly = [[] for _ in range(n+1)]
    visited=[False]*(n+1)
    for i in range(m):
        x,y = map(int,input().split())
        familly[y].append(x)
        familly[x].append(y)

    print(bfs(a,b))