N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
search_list = list(map(int, input().split()))

# A 수들이 search_list 에 존재하는가 확인하기
# 이분 탐색

for b in search_list:
    left = 0
    right = M
    flag = False
    while left < right:
        mid = (left + right) // 2
        # 찾은 경우
        if A[mid] == b:
            flag = True
            break
        # 중간값이 기준값보다 작은 경우 -> 좌측은 안봐도됨
        elif A[mid] < b:
            left = mid + 1
        # 중간값이 기준값보다 큰 경우 -> 우측은 안봐도됨
        elif A[mid] > b:
            right = mid
    
    print(1 if flag else 0)





