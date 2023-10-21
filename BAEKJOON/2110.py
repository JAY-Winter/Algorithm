'''
- 집 N개가 수직선 위에 있다.
    각각의 집의 좌표는 x1, ... xN 이다

- 집에 공유기 C 개를 설치하고자 한다
    최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에
    한 집에는 공유기를 하나만 설치할 수 있고
    가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하고자 한다

Q) C 개의 공유기를 N 개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하라
    출력 : 가장 인접한 두 공유기 사이의 최대 거리를 구하라
'''

# 집 <= 200,000
N, C = map(int, input().split())
# 집의 좌표 <= 1,000,000,000
homes = []
for _ in range(N):
    x = int(input())
    homes.append(x)

homes = sorted(homes)

answer = 0

# start : 두 집 사이의 최소 거리
# end : 가장 먼 집과 가장 가까운 집 사이의 거리
start, end = 1, homes[-1] - homes[0]
while start <= end:
    mid = (start + end) // 2  # 가장 인접한 두 공유기 사이의 거리
    prev_home = homes[0]  # 첫 번째 집에는 항상 공유기를 설치한다
    count = 1  # 첫 번째 집에 공유기 설치된 것을 계산

    # 공유기 설치
    for i in range(1, N):
        if homes[i] - prev_home >= mid:  # mid보다 큰 거리에 있는 집에 공유기 설치
            count += 1
            prev_home = homes[i]

    # 공유기의 개수를 기준으로 이진 탐색 범위 조절
    if count >= C:  # C 개 이상의 공유기를 설치할 수 있는 경우 -> 공유기 설치 간격이 작다는 뜻
        start = mid + 1
        answer = mid
    else:  # C 개 이상의 공유기를 설치할 수 없는 경우 -> 공유기 설치 간격이 크다는 뜻
        end = mid - 1

print(answer)
