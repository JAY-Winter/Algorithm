n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

left = 0
right = n-1

cnt = 0
while left < right:
    temp = nums[left] + nums[right]

    if temp < x:
        left += 1
    elif temp > x:
        right -= 1
    elif temp == x:
        right -= 1
        cnt += 1

print(cnt)