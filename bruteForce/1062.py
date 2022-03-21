#가르침 22-03-19
import sys
input = sys.stdin.readline

def dfs(idx,cnt):
    global answer
    if cnt==k-5:
        readcnt=0
        for word in words:
            check=True
            for w in word:
                if not learn[ord(w)-ord('a')]:
                    check=False
                    break
            if check:
                readcnt+=1
        answer = max(answer,readcnt)
        return
    for i in range(idx,26):
        if not learn[i]:
            learn[i]=True
            dfs(i,cnt+1)
            learn[i]=False


if __name__ == '__main__':
    n,k = map(int,input().split())

    #k가 5보다 작으면 어떤 언어도 배울 수 없음
    if k<5:
        print(0)
    #k가 26이면 모든 언어를 배울 수 있음
    elif k==26:
        print(n)
    else:
        answer = 0
        words = [set(input().strip()) for _ in range(n)]
        learn = [0]*26

        #적어도 언어 하나는 배우기 위해 a,c,i,n,t는 배워야 한다.
        for c in ('a','n','t','i','c'):
            learn[ord(c)-ord('a')]=1

        dfs(0,0)
        print(answer)