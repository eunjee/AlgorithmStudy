#모든 길드원들이 모험을 떠날 필요는 없다.
#공포도가 적은 순으로 팀을 구성해야 많은 팀을 구성할 수 있다.

if __name__ == '__main__':
    n = int(input())
    data=list(map(int,input().split()))
    data.sort()
    count=0
    result=0
    for d in data:
        count+=1
        if count>=d:
            count=0
            result+=1
    print(result)
