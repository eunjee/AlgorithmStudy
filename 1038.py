#감소하는수
from itertools import combinations
if __name__ == '__main__':
    n = int(input())
    nums = list()
    for i in range(1,11):
        for comb in combinations(range(0,10),i):
            comb = list(comb)
            comb.sort(reverse=True) #해당 조합을 감소하는 수로 변경
            nums.append(int("".join(map(str,comb))))
    nums.sort()

    try:
        print(nums[n])
    except:
        print(-1)
