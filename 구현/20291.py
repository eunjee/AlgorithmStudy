import sys
input = sys.stdin.readline
if __name__=='__main__':
    file={}
    n=int(input())
    for _ in range(n):
        fileName,extension = input().split('.')
        if not extension in file:
            file[extension]=0
        file[extension]+=1
    keys=sorted(file.items())
    for key,value in keys:
        print(key.rstrip(),value)
