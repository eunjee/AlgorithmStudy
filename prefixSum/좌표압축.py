#n개의 점이 수직선 상에 존재
#m개의 쿼리를 처리
#쿼리는 x~y구간에 있는 점의 수를 출력하는 쿼리
from bisect import bisect_left
n = int(input())
idx = [0]*(n+1)
for i in range(n):
    idx[i]=int(input())

m = int(input())
for i in range(m):
    x,y = map(int,input().split())
    idx.append(x)
    idx.append(y)

idx.sort()

dedup = list(set(idx)) #중복을 없앤 리스트

def get_idx(x):
    return bisect_left(dedup,x) - dedup[0]
