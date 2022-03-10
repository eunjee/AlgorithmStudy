
if __name__ == '__main__':
    data =list(map(int,input()))
    result=data[0]
    for d in data[1:]:
        if result<=1 or d<=1:
            result+=d
        else:
            result*=d
    print(result)