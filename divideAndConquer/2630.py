#색종이 만들기 22-02-16

def divide(x,y,n):
    tmp = confeti[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if confeti[i][j]!=tmp:#색이 다르면 divide
                divide(x,y,n//2)#왼쪽 위
                divide(x,y+n//2,n//2) #오른쪽 위
                divide(x+n//2,y,n//2)#왼쪽 아래
                divide(x+n//2,y+n//2,n//2)#오른쪽 아래
                return
    result.append(tmp) #각자 색


if __name__=='__main__':
    n = int(input())
    confeti=[list(map(int,input().split())) for _ in range(n)]
    result=[]

    divide(0,0,n)
    print(result.count(0))
    print(result.count(1))