#숨바꼭질 3 22-03-04
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = 100001
if __name__=='__main__':
    n,k = map(int,input().split())
    visited=[0]*(INF)
    q = []
    heappush(q,(0,n))#time과 현재위치

    while q:
        time,curr = heappop(q)
        if curr==k:
            print(time)
            break
        next = [curr-1,curr+1,curr*2]
        for ne in next:
            if 0<=ne<INF and visited[ne]==0:#방문한 적이 없다면
                visited[ne]=1
                if ne==curr*2:
                    heappush(q,(time,ne))
                else:
                    heappush(q,(time+1,ne))
