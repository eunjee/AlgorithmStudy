#입국심사 22-01-28
n,m = map(int,input().split()) #입국심사대, 사람수
time =[0]*(n) #입국심사대에서 걸리는 시간
for i in range(n):
    t = int(input())
    time[i]=t

#총 시간을 기준으로 이분 탐색
start = min(time) #최소시간
end=max(time)*m #최대시간
answer=0
while start<=end:
    mid = (start+end)//2
    count=0
    for t in time:
        count+=mid//t #주어진 시간동안 심사할 수 있는 사람 수

    if count<m: #사람 수 적으면? 시간을 늘려라
        start=mid+1
    else:
        end=mid-1
        answer=mid
print(answer)