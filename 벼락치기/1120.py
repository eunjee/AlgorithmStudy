if __name__ == '__main__':
    A,B = input().strip().split()
    diff=len(B)-len(A)
    length = len(B)
    count = int(1e9)
    if diff==0:
        count=0
        for i in range(len(A)):
            if A[i]!=B[i]:
                count+=1
        print(count)
    else:
        for i in range(0,diff+1):
            tmp=B[:diff-i]+A+B[length-i:length]
            curr=0
            for k in range(length):
                if tmp[k]!=B[k]:
                    curr+=1
            count=min(curr,count)
        print(count)
