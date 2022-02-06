#세 용액 22-02-06 이분 탐색
#2467번에서 용액 하나를 추가로 고정시킨다.
import sys

def solution(n,liquid):
    liquid.sort() #정렬하기
    start =1
    end = n - 1  # 마지막
    answer = [liquid[0], liquid[start], liquid[end]]
    min_val = abs(liquid[0] + liquid[start] + liquid[end])
    for fix in range(n-2): #범위 - 3개 골라야 함
        start = fix+1
        end = n - 1  # 마지막
        while start<end:
            mix = liquid[fix]+liquid[start]+liquid[end]
            if abs(mix)<min_val:
                min_val = abs(mix)
                answer[0] = liquid[fix]
                answer[1]=liquid[start]
                answer[2]=liquid[end]
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


