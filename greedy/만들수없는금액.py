if __name__ == '__main__':
    n = int(input())
    coin = list(map(int,input().split()))
    coin.sort()
    target = 1
    for x in coin:
        if target<x: #만들 수 없는 금액을 찾은 경우
            break
        target+=x
    print(target)

