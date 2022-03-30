#스타트링크 22-03-30
#총 F층으로 이루어진 고층 건물, 스타트 링크가 있는 곳은 G층
#강호는 S층이고, 엘베를 타고 G층으로 이동
#업, 다운만 있음
import sys
from collections import deque
input = sys.stdin.readline

def bfs(S,G):
    q = deque()
    q.append((S, 0))  # 시작 층, count
    visited[S] = True  # 방문 표시
    while q:
        curr, count = q.popleft()
        if curr == G:
            return count
        # up
        if curr + U < F + 1 and not visited[curr+U]:
            q.append((curr + U, count + 1))
            visited[curr+U]=True
        # down
        if curr - D >0 and not visited[curr-D]:
            q.append((curr - D, count + 1))
            visited[curr-D]=True

    return "use the stairs";

if __name__ == '__main__':
    F,S,G,U,D = map(int,input().split())
    visited = [False]*(F+1) #전체 층

    print(bfs(S,G))