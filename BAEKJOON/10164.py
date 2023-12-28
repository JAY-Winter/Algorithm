'''
오른쪽, 아래 쪽으로만 이동 가능
O 칸이 있는 경우, 반드시 지나가야 함

Q) 두 조건을 만족하면서 N,M 번칸으로 이동할 수 있는 서로 다른 경로가 총 몇 개인가
'''

from collections import deque

def search(start_point_r, start_point_c, end_point_r, end_point_c):
    # 오른쪽, 아래
    dr = [0, 1]
    dc = [1, 0]
    cnt = 0

    Q = deque()
    Q.append((start_point_r, start_point_c))
    while Q:
        r, c = Q.popleft()

        # K 에 도달한 경우
        if r == end_point_r and c == end_point_c:
            cnt += 1

        for d in range(2):
            nr, nc = r + dr[d], c + dc[d]
            # 격자 범위 내
            if N > nr >= 0 and M > nc >= 0:
                Q.append((nr, nc))

    return cnt


N, M, K = map(int, input().split())

board = [[0 for _ in range(M)] for _ in range(N)]

answer = 0

K_valid = False
if K:
    point_r = (K - 1) // M
    point_c = K % M - 1
    board[point_r][point_c] = K
    K_valid = True

    answer += search(0, 0, point_r, point_c)
    answer *= search(point_r, point_c, N - 1, M - 1)
else:
    answer += search(0, 0, N - 1, M - 1)
print(answer)
