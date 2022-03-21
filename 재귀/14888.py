#연산자 끼워넣기
import sys
input = sys.stdin.readline
def recursion(idx,tmp):
    global min_val
    global max_val
    if idx==n:
        min_val = min(tmp,min_val)
        max_val = max(tmp,max_val)
        return
    else:
        if op[0]!=0:
            op[0]-=1
            recursion(idx+1,tmp+nums[idx])
            op[0]+=1
        if op[1]!=0:
            op[1]-=1
            recursion(idx+1,tmp-nums[idx])
            op[1]+=1
        if op[2]!=0:
            op[2]-=1
            recursion(idx+1,tmp*nums[idx])
            op[2]+=1
        if op[3]!=0:
            op[3]-=1
            if tmp<0:
                recursion(idx+1,-(abs(tmp)//nums[idx]))
            else:
                recursion(idx+1,tmp//nums[idx])
            op[3]+=1
    return
if __name__ == '__main__':
    n = int(input())
    nums=list(map(int,input().split()))
    op =list(map(int,input().split())) #더하기 빼기 곱하기 나누기

    min_val = int(1e9)
    max_val = -int(1e9)

    recursion(1,nums[0])

    print(max_val)
    print(min_val)