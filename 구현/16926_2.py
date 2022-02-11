#22-02-10 배열돌리기 수정
import sys
input = sys.stdin.readline
n,m,r = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)] #입력받기

def rotate(time,i):
    for _ in range(time):
        start=i
        left=arr[n-start-1][start]
        bottom=arr[n-start-1][m-start-1]
        right=arr[start][m-start-1]
        top=arr[start][start]
        #좌 -> 아래로 이동
        for j in range(n-start-1,start,-1):
            arr[j][start]=arr[j-1][start]
        #하->오른쪽으로 이동
        for j in range(m-start-1,start+1,-1):
            arr[n-start-1][j]=arr[n-start-1][j-1]
        #우->위로 이동
        for j in range(start+1,n-start):
            arr[j-1][m-start-1]=arr[j][m-start-1]
        #상-> 왼쪽으로 이동
        for j in range(start+1,m-start):
            arr[start][j-1]=arr[start][j]
        arr[start+1][start]=top
        arr[n-start-1][start+1]=left
        arr[n-start-2][m-start-1]=bottom
        arr[start][m-start-2]=right

for i in range(min(n,m)//2):
    time = r%(2*(m-i*2)+2*(n-i*2)-4)
    rotate(time,i)

for i in range(n):
    print(*arr[i])