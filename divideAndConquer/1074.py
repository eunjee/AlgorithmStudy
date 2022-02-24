#Z 22-02-19 (오답)
import sys
input = sys.stdin.readline

def search(sx,sy,size):
    global count
    if size==2:
        if sx==r and sy==c: #2사분면
            print(count)
            return
        count+=1
        if sx==r and sy+1==c:
            print(count)
            return
        count+=1
        if sx+1==r and sy==c:
            print(count)
            return
        count+=1
        if sx+1==r and sy+1==c:
            print(count)
            return
        count+=1

    else:
        search(sx,sy,size//2) # 제 2사분면
        search(sx,sy+size//2,size//2)# 제 1사분면
        search(sx+size//2,sy,size//2)# 제 3사분면
        search(sx+size//2,sy+size//2,size//2)# 제 4사분면

if __name__=='__main__':
    n,r,c = map(int,input().split())
    count=0

    search(0,0,2**n)
