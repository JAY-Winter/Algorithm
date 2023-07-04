N, M = map(int, input().split())


# 만약 M 개를 전부 고름 => 조건에 맞는 탐색을 한 가지 성공한 것
# 아직 M 개를 고르지 않음 => k 번째 부터 M 번째 원소를 조건에 맞게 고르는 모든 방법을 시도한다
def rec_func(start,seq, n):
    if n == M:
        print(' '.join(map(str, seq)))
        return
    
    for i in range(start, N+1):
        rec_func(i, seq + [i], n+1)

rec_func(1, [], 0)

# [0]
# [0, 0]
# [1]
# [1, 0]
# [1, 1]
