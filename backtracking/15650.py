from itertools import combinations


if __name__=='__main__':
    n,m = map(int,input().split())
    comb = combinations(range(1,n+1),m)

    for c in comb:
        print(*c)