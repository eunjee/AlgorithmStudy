#랜선자르기 복습
k, n = map(int, input().split())
cable = []
for _ in range(k):
    cable.append(int(input()))
# 이분탐색
start = 1
end = max(cable)
answer = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for c in cable:
        count += c // mid
    if count < n:  # 길이를 줄여라
        end = mid - 1
    else:  # 길이를 늘려라
        start = mid + 1
        answer = mid

print(answer)