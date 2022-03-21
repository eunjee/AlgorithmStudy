#가르침 22-03-22 시간초과 ㄱ-
from itertools import combinations
import sys
input = sys.stdin.readline
if __name__ == '__main__':
    answer=0
    n,k = map(int,input().split())
    words = [input().strip() for _ in range(n)] #단어들 입력
    learn = []
    #배워야 하는 알파벳 개수
    for w in words:
        tmp = set(w)
        if len(tmp)<=k:
            learn.append(tmp)
    if len(learn)==0:
        print(0)
        sys.exit(0)
    #모든 단어 못 배움
    if k<5:
        print(0)
    #모든 단어 배울 수 있음
    elif k==26:
        print(n)
    #브루트 포스
    else:
        for i in range(len(learn),1,-1):
            for comb in combinations(learn,i):
                tmp=set()
                for c in comb:
                    tmp = tmp.union(c)
                if len(tmp)<=k:
                    answer = i
                    break
            if answer!=0:
                break
        if answer==0:
            print(1)
        else:
            print(answer)