

def rotate_clockwise(n,arr):
    count=1
    for i in range(round(n/2)+1):
        start = count
        for j in range(i,n-i-1):
            arr[i][j]=start
            arr[j][n-1-i]=start
            arr[n-1-i][n-1-j]=start
            arr[n-1-j][i]=start
            start+=1
        if i==n-i-1:
            arr[i][i]=start
        count=start


def rotate_counter_clockwise(n,arr):
    count = 1
    for i in range(round(n / 2)+1):
        start = count
        for j in range(i, n - i - 1):
            arr[i][n - 1 - j] = start
            arr[j][i] = start
            arr[n-1-i][j] = start
            arr[n-1-j][n-i-1]=start
            start += 1

        if i == n - i - 1:
            arr[i][i] = start
        count = start

def solution(n,clockwise):
    answer =0
    arr = [[0]*n for _ in range(n)]
    if clockwise:
        rotate_clockwise(n,arr)
    else:
        rotate_counter_clockwise(n,arr)
    return arr

answer = solution(5,True)
for i in range(5):
    print(*answer[i])