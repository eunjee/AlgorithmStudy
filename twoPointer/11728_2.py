#배열합치기 22-03-05
import sys
input = sys.stdin.readline
if __name__=='__main__':
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    answer = a+b
    answer.sort()
    print(*answer)