#맥주 걸어가기 복습 22-02-05
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    visited=[False]*(n+1) #가게의 개수를 인덱스로 방문 리스트 생성

    while q:
        x,y = q.popleft()
        if x==dest[0] and y==dest[1]: #목적지에 도착했다면 happy
            print("happy")
            return
        for idx,location in enumerate(store):
            if visited[idx]==False:
                if abs(location[0]-x)+abs(location[1]-y)<=1000: #50m*20병 이므로 1000m 보다 가까우면 방문한다.
                    visited[idx]=True
                    q.append(location)
    print("sad") #도착 못하고 끝냈다면 sad
    return


t = int(input())
for _ in range(t):
    n = int(input())
    house=list(map(int,input().split()))
    store = [list(map(int,input().split())) for i in range(n+1)] #편의점 리스트를 입력받을 때 목적지까지 받도록 한다.
    dest = store[-1]
    bfs(house)