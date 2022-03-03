#합이 0 22-03-03
import sys
input = sys.stdin.readline

def select_team():
    count=0
    max_idx=n
    for i in range(n-2): #한 명은 고정
        start,end = i+1,n-1 #고정 다음, 맨 끝
        while start<end:
            weight=arr[i]+arr[start]+arr[end]
            if weight==0:
                if arr[start]==arr[end]:
                    count+=end-start
                else:
                    if max_idx> end:
                        max_idx=end
                        while max_idx>=0 and arr[max_idx-1]==arr[end]:
                            max_idx-=1
                    count+=end-max_idx+1
                start+=1
            elif weight<0:
                start+=1
            else:
                end-=1
    print(count)


n = int(input())
arr = list(map(int,input().split()))
arr.sort()
select_team()