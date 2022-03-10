import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    A=list(map(int,input().split()))
    A_dict = dict.fromkeys(A,1)
    m = int(input())
    B=list(map(int,input().split()))

    for b in B:
        if b in A_dict:
            print(1)
        else:
            print(0)