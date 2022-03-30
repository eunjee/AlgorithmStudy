if __name__ == '__main__':
    a,b = map(int,input().split())
    arr=[]
    for i in range(1,b+1):
        for j in range(i):
            if len(arr)==b:
                break
            arr.append(i)

    print(sum(arr[a-1:b]))