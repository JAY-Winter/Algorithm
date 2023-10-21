'''
가능한 한 최대의 총 예산을 아래의 방법으로 배정한다
1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다
2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여
    그 이상인 예상 요청에는 모두 상한액을 배정한다.
    상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다

예) 전체 국가예산이 120, 110, 140, 150 이고 상한액이 127일 경우
120, 110, 127, 127 을 배정하고 그 합이 484로 가능한 최대가 된다

'''

# N: 지방의 수
N = int(input())

# requests : 각 지방의 예산요청 금액
requests = list(map(int, input().split()))

# M : 총 예산
M = int(input())

answer = 0
start, end = 1, max(requests)

while start <= end:
    mid = (start + end) // 2

    total_amount = 0
    for request in requests:
        if request > mid:
            total_amount += mid
        else:
            total_amount += request

    if total_amount > M:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)
