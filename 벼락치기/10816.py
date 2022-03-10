import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    A= list(map(int,input().split()))
    m = int(input())
    B= list(map(int,input().split()))
    dictionary = {}
    for a in A:
        if a not in dictionary:
            dictionary[a]=1
        else:
            dictionary[a]+=1
    for b in B:
        if b not in dictionary:
            print(0,end=" ")
        else:
            print(dictionary[b],end=" ")