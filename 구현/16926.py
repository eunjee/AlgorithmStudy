#배열돌리기_반시계 틀림 (r번 회전 대신에 한번에 r만큼 이동할 수 있도록 한다.)
import sys
input = sys.stdin.readline
n,m,r = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

for _ in range(r): #회전의 수
    for i in range(min(n,m)//2): #회전 사각형의 수
        sx,sy=i,i
        curr_value=arr[i][i]
        #좌,하,우,상의 순서로 회전
        for k in range(i+1,n-i): #아래로 이동
            sx=k
            prev_value=arr[sx][sy]
            arr[sx][sy]= curr_value
            curr_value=prev_value
        for k in range(i+1,m-i):#오른쪽으로 이동
            sy=k
            prev_value=arr[sx][sy]
            arr[sx][sy]=curr_value
            curr_value=prev_value
        for k in range(i+1,n-i): #위로 이동
            sx=n-k-1
            prev_value=arr[sx][sy]
            arr[sx][sy]=curr_value
            curr_value=prev_value
        for k in range(i+1,m-i): #왼쪽으로 이동
            sy=m-k-1
            prev_value=arr[sx][sy]
            arr[sx][sy]=curr_value
            curr_value=prev_value

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()
