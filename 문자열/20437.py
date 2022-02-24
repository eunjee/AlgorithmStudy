#문자열 게임2 22-02-22
from collections import defaultdict
import sys
input = sys.stdin.readline
def game(strings):
    length = len(strings)
    alpha = defaultdict(list)
    for i in range(length):
        if strings.count(strings[i]) >= k:
            alpha[strings[i]].append(i)  # 인덱스 추가

    if not alpha:  # 3번 조건
        return (-1,)
    max_len = 0
    min_len = 10000
    for idx_list in alpha.values():
        for j in range(len(idx_list) - k + 1):
            tmp = idx_list[j + k - 1] - idx_list[j] + 1  # 문자 k개를 포함하는 문자열의 길이
            if tmp > max_len:
                max_len = tmp
            if tmp < min_len:
                min_len = tmp
    return min_len,max_len

t = int(input())
for _ in range(t):
    strings = input().strip()
    k = int(input())
    print(*game(strings))
