
import sys
input = sys.stdin.readline

n = int(input())

town =[]

for _ in range(n):
    index,people = map(int,input().split())
    town.append([index,people])

town = sorted(town,key=lambda x:x[0])

total=0
for i,w in town:
    total+=w

mid = total//2
if total%2==1:
    mid+=1

answer=0
#인구 수가 절반이 되는 순간이 마을의 우체국
for i,w in town:
    answer+=w
    if answer>=mid:
        print(i)
        break
