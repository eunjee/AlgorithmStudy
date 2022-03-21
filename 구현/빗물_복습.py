#14719 빗물 복습

if __name__ == '__main__':
    h,w = map(int,input().split())
    data = list(map(int,input().split()))

    answer = 0
    for i in range(1,w-1):
        left = max(data[:i]) #왼쪽 최대
        right = max(data[i+1:]) #오른쪽 최대

        compare = min(left,right)
        if compare>data[i]:
            answer+=compare-data[i]

    print(answer)