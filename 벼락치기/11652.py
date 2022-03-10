import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    cards={}
    for _ in range(n):
        t = int(input())
        if t not in cards:
            cards[t]=1
        else:
            cards[t]+=1
    result=sorted(cards.items(),key=lambda x:(-x[1],x[0]))
    print(result[0][0])