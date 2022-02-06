#용액 22-02-06
import sys

def solution(n,liquid):
    liquid.sort() #정렬하기
    start = 0
    end=n-1 #마지막
    answer=[liquid[start],liquid[end]]
    min_val=abs(liquid[start]+liquid[end])

    while start<end:
        mix = liquid[start]+liquid[end]
        if abs(mix)<min_val:
            min_val = abs(mix)
            answer[0]=liquid[start]
            answer[1]=liquid[end]
        if mix>0: #end를 앞으로 옮겨준다.
            end-=1
        elif mix<0: #start를 뒤로 옮겨준다.
            start+=1
        else:
            print(*answer)
            return answer
    print(*answer)
    return answer

if __name__=="__main__":
    input = sys.stdin.readline
    n = int(input())
    liquid = list(map(int,input().split()))
    solution(n,liquid)


