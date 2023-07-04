T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    # N, M <= 20,000
    # A 의 크기가 B 보다 큰 쌍이 몇 개나 있는지 구하라
    
    cnt = 0
    for a in A:
        left = 0 
        right = M
        
        while left < right:
            mid = (left + right) // 2
            if a == 8:
                print('mid',B[mid], mid, left)
            if a > B[mid]:
                left = mid + 1
            else:
                right = mid
        cnt += left

    print(cnt)