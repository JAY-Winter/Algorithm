def isGood(index):
    num = nums[index]
    start, end = 0, N - 1

    while start < end:
        if start == index:
            start += 1
            continue
        if end == index:
            end -= 1
            continue

        SUM = nums[start] + nums[end]

        if SUM == num:
            return True

        if SUM > num:
            end -= 1
        else:
            start += 1

    return False

# 수의 개수
N = int(input())
# nums <= 1억 -> 완탐불가 -> 이분탐색
nums = list(map(int, input().split()))
nums.sort()

answer = 0

# 모든 nums 를 순회하면서 해당 num 이 만들어지는지? 확인?
for i in range(N):
    if isGood(i):
        answer += 1

print(answer)
