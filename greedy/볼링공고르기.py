if __name__ == '__main__':
    n,m = map(int,input().split())
    data = list(map(int,input().split()))
    arr=[0]*11 #최대 무게 공
    result=0
    for x in data:
        arr[x]+=1 #개수 추가
    #2개를 고를 때 서로 다른 무게를 선택
    for i in range(1,m+1):
        n-=arr[i]
        result+=arr[i]*n

    print(result)