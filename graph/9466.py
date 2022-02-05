#텀프로젝트 22-01-30
import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)
def dfs(i):
    global ans
    visited[i]=True
    cycle.append(i) #사이클을 이루는 팀을 확인하기 위함
    num = team[i]
    if visited[num]: #방문가능한 곳이 끝났는지
        if num in cycle: #사이클 가능 여부
            ans += len(cycle[cycle.index(num):])
        return
    else:
        dfs(num)

t = int(input())
for _ in range(t):
    n = int(input())
    team = [0]+list(map(int,input().split()))
    visited=[False]*(n+1)
    ans=0
    for i in range(1,n+1):
        if not visited[i]: #방문하지 않았다면
            cycle=[]
            dfs(i)
    print(n-ans)