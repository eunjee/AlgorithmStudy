#촌수계산 22-01-30
from collections import deque
import sys

input = sys.stdin.readline

n = int(input()) #전체 사람의 수
a,b = map(int,input().split()) #촌 수 계산해야 하는 사람
m = int(input())

arr =[[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split()) #x는 y의 부모
    arr[x].append(y)
    arr[y].append(x)

def bfs():
    q = deque()
    q.append((a,0))#시작, 촌 수
    visited=[False]*(n+1)
    visited[a]=True

    while q:
        curr,dist = q.popleft()
        for i in arr[curr]:
            if not visited[i]:
                if i==b:
                    print(dist+1)
                    return
                else:
                    q.append((i,dist+1))
                    visited[i]=True
    print(-1)

bfs()


