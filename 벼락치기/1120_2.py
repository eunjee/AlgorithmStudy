if __name__ == '__main__':
    #비교하고자 하는 문자열을 통째로 옮겨서 개수 세기
    a,b = input().strip().split()
    answer=[]
    for i in range(len(b)-len(a)+1):
        count=0
        for j in range(len(a)):
            if a[j]!=b[i+j]:
                count+=1
        answer.append(count)
    print(min(answer))