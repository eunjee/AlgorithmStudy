if __name__=='__main__':
    while True:
        n = int(input())
        if n==0:
            break
        dobby=[]
        for _ in range(n):
            dobby.append(input().strip())

        dobby.sort(key = lambda x:x.lower())
        print(dobby[0])