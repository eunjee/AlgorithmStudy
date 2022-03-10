if __name__ == '__main__':
    data=list(input())
    count0=0
    count1=0
    if data[0]=='0':
        count0+=1
    else:
        count1+=1

    for i in range(1,len(data)):
        if data[i-1]!=data[i]:
            if data[i]=='0':
                count0+=1
            else:
                count1+=1
    print(min(count0,count1))