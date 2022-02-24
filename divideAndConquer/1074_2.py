#Z 22-02-19
#참고 - https://www.acmicpc.net/board/view/64976
if __name__=='__main__':
    n,r,c = map(int,input().split())
    ans=0
    while n>0:
        n -= 1
        size = 2**n
        if r<size and c<size: #2사분면 내에 존재
            continue
        elif r<size and c>=size: #1사분면
            ans+=size**2
            c-=size
        elif r>=size and c<size: #3사분면
            ans+=size**2*2
            r-=size
        elif r>=size and c>=size:
            ans+=size**2*3
            r-=size
            c-=size
    print(ans)
