#회문 22-02-22
n = int(input())

def is_palindrome():
    flag = 0

    for i in range(length//2):
        #글자가 다르면
        if strings[i]!=strings[length-i-1]:
            for j in range(i,length//2): #앞글자 삭제해서 탐색
                if strings[j+1]!=strings[length-j-1]:
                    flag+=1
                    break
            for j in range(i,length//2): #뒷글자 삭제해서 탐색
                if strings[j]!=strings[length-j-2]:
                    flag+=1
                    break
            if flag==1 or flag==0:
                print(1)
                return
            elif flag==2:
                print(2)
                return
    print(0)
    return

for _ in range(n):
    strings = list(input())#문자열 리스트로 받기
    length = len(strings)

    is_palindrome()




