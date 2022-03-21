#3번 문제
from math import factorial
def solution(width,height,edges):
    sx,sy=1,1
    answer =0
    for ex,ey in edges:
        lx,ly = ex+1,ey #왼쪽 위
        rx,ry = ex,ey+1 #오른쪽 아래
        prev = factorial((lx-sx)+(ly-sy))//(factorial(lx-sx)*factorial(ly-sy)) #왼쪽 위까지의 경로
        next = factorial((width-rx+1)+(height-ry+1))//(factorial(width-rx+1)*factorial(height-ry+1)) #대각선 건넌 후 오른쪽 아래에서 끝까지의 경로
        answer+= prev*next
        prev = factorial((rx - sx) + (ry - sy)) // (factorial(rx - sx) * factorial(ry - sy)) #오른쪽아래까지의 경로
        next = factorial((width - lx + 1) + (height - ly + 1)) // (factorial(width - lx + 1) * factorial(height - ly + 1)) #대각선 건넌 후 왼쪽 아래에서의 경로
        answer += prev*next
    print(answer%10000019)

if __name__ == '__main__':
    width=250
    height=250
    diagonals=[[17,19]]
    solution(width,height,diagonals)

