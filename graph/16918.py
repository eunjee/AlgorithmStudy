#봄버맨 22-02-04
import sys
input = sys.stdin.readline
dx=[-1,1,0,0]
dy=[0,0,-1,1]


r,c,n = map(int,input().split())
bomb = [list(input().rstrip()) for _ in range(r)]#그래프 입력받기
#1초면 바로 출력
if n==1:
    for b in bomb:
        print(''.join(b))
#짝수 초 -> 모두 0인 칸으로
elif n%2==0:
    answer = [['O'] * c for _ in range(r)]
    for a in answer:
        print(''.join(a))

#홀수 초 -> 터뜨리고 나머지 0으로 바꾸기
else:
    tmp1 = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if bomb[i][j]=='O': tmp1[i][j]='.'
            else:
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<r and 0<=ny<c:
                        if bomb[nx][ny]=='O':
                            tmp1[i][j]='.'
                            break

    tmp2 = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if tmp1[i][j]=='O': tmp2[i][j]='.'
            else:
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<r and 0<=ny<c:
                        if tmp1[nx][ny]=='O':
                            tmp2[i][j]='.'
                            break
    if n%4==3:
        for t in tmp1:
            print(''.join(t))
    if n%4==1:
        for t in tmp2:
            print(''.join(t))
