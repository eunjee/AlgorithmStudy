# import sys
# input = sys.stdin.readline

strings=list(input().rstrip())
answer=[]
def findNext(prev,curr):
    for a in answer:
        if a[-1]==prev:
            a.append(curr)
            return True
    return False

flag=0
for s in strings:
    if s=='q':
        if not findNext('k','q'):
            answer.append(['q']) #새로운 리스트를 추가
    elif s=='u':
        if not findNext('q', 'u'):
            flag=1
            break
    elif s=='a':
        if not findNext('u', 'a'):
            flag = 1
            break
    elif s=='c':
        if not findNext('a', 'c'):
            flag = 1
            break
    else:
        if not findNext('c', 'k'):
            flag = 1
            break
count=0
for a in answer:
    if 'quack' in ''.join(a) and len(a)%5==0:
        count+=1
    else:
        flag=1
        break
if flag==1:
    print(-1)
else:
    print(count)

