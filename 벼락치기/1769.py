def recursion(string,count):
    if len(string)>1:
        tmp=0
        for s in string:
            tmp +=int(s)
        recursion(str(tmp),count+1)
    else:
        print(count)
        if int(string)%3==0:
            print("YES")
        else:
            print("NO")
if __name__ == '__main__':
    x = input()
    count=0
    recursion(x,0)