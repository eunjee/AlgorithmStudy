#다이얼
if __name__ == '__main__':
    strings = input().strip()
    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    answer = 0
    for s in strings:
        for i in range(len(dial)):
            if s in dial[i]:
                answer+= i+3
    print(answer)