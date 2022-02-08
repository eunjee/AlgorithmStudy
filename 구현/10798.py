#세로 읽기 22-02-08


if __name__ == '__main__':
    strings = [list(input().rstrip()) for _ in range(5)]
    answer=[]

    #빈공간에 0채우기
    max_len = 0
    for i in range(5):
        max_len=max(len(strings[i]),max_len)
    for i in range(5):
        while max_len>len(strings[i]):
            strings[i].append('*')
    for i in range(max_len):
        answer.extend([k[i] for k in strings])

    result = ''.join(answer).replace('*','')
    print(result)

