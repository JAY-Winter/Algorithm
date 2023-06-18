N, M = map(int, input().split())
selected = []

# 만약 M 개를 전부 고름 => 조건에 맞는 탐색을 한 가지 성공한 것
# 아직 M 개를 고르지 않음 => k 번째 부터 M 번째 원소를 조건에 맞게 고르는 모든 방법을 시도한다
def rec_func(n, nums):
    if n == M:
        print(nums)
        return
    
    for i in range(1, N+1):
        i = str(i)
        rec_func(n+1, nums+i+' ')

rec_func(0, '')