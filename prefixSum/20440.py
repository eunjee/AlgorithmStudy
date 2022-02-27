import heapq
import sys
input = sys.stdin.readline
n = int(input())
count = 0
range_answer =[0,0]
mos_time = [tuple(map(int,input().split())) for _ in range(n)] #입력받기
mos_time.sort() #시작 시간 기준으로 정렬

heap=[]
for mos_start,mos_end in mos_time:
    if heap and heap[0][0]<=mos_start:
        heapq.heappop(heap)

    heapq.heappush(heap,(mos_end,mos_start))
    if len(heap) == count and range_answer[1]==mos_start:
        range_answer[1]=heap[0][0] #끝나는 시간 업데이트
    elif len(heap)>count:
        count = len(heap)
        range_answer = [mos_start,heap[0][0]]

print(count)
print(range_answer[0],range_answer[1])

