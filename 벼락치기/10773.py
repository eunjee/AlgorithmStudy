import sys
input = sys.stdin.readline
if __name__ == '__main__':
    k=int(input())
    stack=[]
    for i in range(k):
        n = int(input())
        if n==0:
            stack.pop()
        else:
            stack.append(n)
    print(sum(stack))