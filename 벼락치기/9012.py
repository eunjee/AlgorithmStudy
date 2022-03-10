import sys
input = sys.stdin.readline
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        flag = False
        string = input().strip()
        stack=[]
        for s in string:
            if s=='(':
                stack.append(s)
            elif stack:
                stack.pop()
            else:
                flag=True
                break

        if len(stack)==0 and not flag:
            print("YES")
        else:
            print("NO")
