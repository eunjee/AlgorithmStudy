#겹치는 건 싫어 22-03-04
if __name__=='__main__':
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    count=[0]*(max(arr)+1)
    answer =0
    start,end = 0,0
    while end<n:
        if count[arr[end]]<k:
            count[arr[end]]+=1
            end+=1
        else:
            count[arr[start]]-=1
            start+=1
        answer = max(answer,end-start)
    print(answer)

