#배열합치기 22-03-05
import sys
input = sys.stdin.readline
if __name__=='__main__':
    n,m = map(int,input().split()) #배열 A,배열 B의 크기
    a = list(map(int,input().split())) #배열 A
    b = list(map(int,input().split())) #배열 B
    answer=[]
    a.sort()
    b.sort()
    a_idx,b_idx = 0,0
    while a_idx<n and b_idx<m:
        if a[a_idx]<=b[b_idx]:
            answer.append(a[a_idx])
            a_idx+=1
        else:
            answer.append(b[b_idx])
            b_idx+=1
    if a_idx<n:
        for i in range(a_idx,n):
            answer.append(a[i])
    else:
        for i in range(b_idx,m):
            answer.append(b[i])
    print(*answer)
