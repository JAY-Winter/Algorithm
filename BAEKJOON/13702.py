'''
N 주전자를 주문하고, 자신을 포함한 K 명에게 막걸리를 똑같은 양으로 분배하려고 함
분배 후 주전자에 막걸리가 남아있가면 버린다

Q) K명에게 최대한의 많은 양의 막걸리를 분배할 수 있는 용량을 구하라
N <= 1만
K <= 1백만
0 <= 막걸리 <= 2^31 - 1

  예를 들어 5명이 3 주전자를 주문하여 1002, 802, 705 ml의 막걸리가 각 주전자에 담겨져 나왔고,
  이것을 401ml로 동등하게 나눴을 경우 각각 주전자에서 200ml, 0m, 304ml 만큼은 버린다.
  -> 2 명, 2 명 , 1명


'''

N, K = map(int, input().split())

volumes = [int(input()) for _ in range(N)]

# Sol) 0 부터 N 주전자 중 가장 큰 값의 중간 값이 target
# target 으로 각 주전자를 나눈 몫의 총합을 result 값과 비교하여 큰 값으로 갱신
result = 0

start = 0
end = max(volumes)

while start <= end:
    target = (start + end) // 2

    # 전체 막걸리를 순회하면서 target 값으로 나눈 몫의 총합 -> 총 몇 개로 배분할 수 있는가
    temp_result = sum(volume // target for volume in volumes)

    # 총 배분 개수가 인원수 보다 같거나 클 경우 -> start 값을 target 보다 키운다
    if temp_result >= K:
        result = target
        start = target + 1
    else:
        end = target - 1

print(result)
