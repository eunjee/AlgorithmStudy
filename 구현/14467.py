#소가 길을 건너간 이유1
n = int(input())
cow={}
answer=0
for i in range(n):
    c,f=map(int,input().split())
    if c in cow:
        if cow[c]!=f:
            answer+=1
    cow[c]=f
print(answer)