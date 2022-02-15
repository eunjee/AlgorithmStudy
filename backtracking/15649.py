#n과m(1) 22-02-14
import sys
from itertools import permutations
input = sys.stdin.readline

if __name__=='__main__':
    n,m = map(int,input().split())

    comb = permutations(range(1,n+1),m)

    for c in comb:
        print(*c)