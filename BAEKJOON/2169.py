# import sys
# sys.setrecursionlimit(10000)

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
## 아래 코드는 시간 복잡도 3^2000 --> 3^(N+M-2) 만큼 걸리기 때문에 안 됨
# visited = [[False] * M for _ in range(N)]
# answer = -987654321

# def dfs(r, c, worth):
#     global answer
#     visited[r][c] = True

#     if r == N-1 and c == M-1:
#         if worth > answer:
#             answer = worth
#         return

#     dr = [0, 0, 1]
#     dc = [-1, 1, 0]
    
#     for d in range(3):
#         new_r = r + dr[d]
#         new_c = c + dc[d]

#         if new_r >= N or new_r < 0 or new_c >= M or new_c < 0:
#             continue

#         if visited[new_r][new_c]:
#             continue

#         new_worth = worth + arr[new_r][new_c]
#         dfs(new_r, new_c, new_worth)
#         visited[new_r][new_c] = False

# init_worth = arr[0][0]
# dfs(0, 0, init_worth)
# print(answer)


import sys

# 입력 받기
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 다이나믹 프로그래밍 테이블 초기화
dp = [[0] * m for _ in range(n)]
dp[0][0] = array[0][0]

# 첫 행 업데이트
for j in range(1, m):
    dp[0][j] = dp[0][j-1] + array[0][j]

# 나머지 행에 대한 DP 테이블 업데이트
for i in range(1, n):
    # 왼쪽에서 오른쪽으로 이동
    left_to_right = [0] * m
    left_to_right[0] = dp[i-1][0] + array[i][0]
    for j in range(1, m):
        left_to_right[j] = max(left_to_right[j-1], dp[i-1][j]) + array[i][j]
    # print(left_to_right)
    # 오른쪽에서 왼쪽으로 이동
    right_to_left = [0] * m
    right_to_left[m-1] = dp[i-1][m-1] + array[i][m-1]
    for j in range(m-2, -1, -1):
        right_to_left[j] = max(right_to_left[j+1], dp[i-1][j]) + array[i][j]
    
    # 현재 행의 DP 테이블 업데이트
    for j in range(m):
        dp[i][j] = max(left_to_right[j], right_to_left[j])
        
print(dp)

print(dp[-1][-1])
