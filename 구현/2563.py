#색종이 22-02-08

back=[[0]*101 for _ in range(101)]

if __name__=="__main__":
    n = int(input())
    papers = [list(map(int,input().split())) for _ in range(n)] #왼쪽 아래 x,y좌표
    answer=0

    #도화지 채우기
    for paper in papers:
        y,x = paper[0],paper[1]
        for i in range(10):
            for j in range(10):
                back[x+i][y+j]=1
    #개수 세기
    for i in range(100):
        for j in range(100):
            if back[i][j]==1:
                answer+=1
    print(answer)