
def compression(x,y,size):
    check = graph[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if check!=graph[i][j]:
                check=-1
                break
    if check==-1:
        print('(',end='')
        size//=2
        compression(x,y,size)
        compression(x,y+size,size)
        compression(x+size,y,size)
        compression(x+size,y+size,size)
        print(')',end='')
    elif check ==1:
        print(1, end='')
    else:
        print(0,end='')


if __name__=='__main__':
    n = int(input())
    graph = [list(map(int,input())) for _ in range(n)]

    compression(0,0,n)
