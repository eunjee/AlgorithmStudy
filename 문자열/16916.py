#부분 문자열 22-02-24 (시간초과)
import sys
input = sys.stdin.readline
if __name__=='__main__':
    strings = input().strip()
    ex = input().strip()
    if ex in strings:
        print(1)
    else:
        print(0)