#n-queen 22-02-15
n = int(input())
answer=0
board=[0]*n

def is_promising(x):
    for i in range(x):
        #같은 열인지 확인 혹은 대각선 방향에 있는지 확인
        if board[x]==board[i] or abs(board[x]-board[i])==abs(x-i):
            return False
    return True

def n_queens(x):
    global answer
    if x==n: #퀸 n개를 놓았을 때
        answer+=1
    else:
        for i in range(n): #[x,i]에 퀸을 놓는 경우
            board[x]=i
            if is_promising(x):
                n_queens(x+1)
n_queens(0)
print(answer)
