import sys
input = sys.stdin.readline

if __name__=='__main__':
    strings=input().rstrip()
    if not '<' in strings:
        list= list(strings.split())
        for li in list:
            print(li[::-1],end=' ')

    else:
        stack=[]
        for s in strings:
            if s=='<':
                print(''.join(stack[::-1]),end='')
                stack=[]
                stack.append('<')
            elif s=='>':
                stack.append('>')
                print(''.join(stack),end='')
                stack=[]
                continue
            elif s==' ' and not '<' in stack:
                print(''.join(stack[::-1]),end=' ')
                stack=[]
            else:
                stack.append(s)
        if stack:
            print(''.join(stack[::-1]),end='')
