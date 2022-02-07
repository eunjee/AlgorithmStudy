#빙고 22-02-07
import sys
input = sys.stdin.readline

bingo = [list(map(int,input().split())) for i in range(5)] #빙고판 입력
mc = [list(map(int,input().split())) for i in range(5)] #사회자 입력
check_row, check_column = [0]*5,[0]*5
check_diag=[0]*2

#불리면 0으로 체크
#가로 체크
def row_check():
    for i in range(5):
        if sum(bingo[i])==0:
            check_row[i]=1


#세로 체크
def column_check():
    for i in range(5):
        if sum(k[i] for k in bingo)==0:
            check_column[i]=1


#왼쪽 위 대각선
def left_diag_check():
    count=0
    for i in range(5):
        for j in range(5):
            if i==j:
                count+=bingo[i][j]
    if count==0:
        check_diag[0]=1


#오른쪽 위 대각선
def right_diag_check():
    count=0
    for i in range(5):
        count+=bingo[4-i][i]
    if count==0:
        check_diag[1]=1

def show():
    for line in bingo:
        print(line)
    print(check_row,check_column,check_diag)

answer=0
for line in mc:
    for target in line: #사회자가 부르는거
        for i in range(5):
            for j in range(5):
                if bingo[i][j]==target:
                    bingo[i][j]=0
                    answer+=1
                    row_check()
                    column_check()
                    left_diag_check()
                    right_diag_check()
                    if sum(check_row)+sum(check_column)+sum(check_diag)>=3:
                        print(answer)
                        exit(0)
