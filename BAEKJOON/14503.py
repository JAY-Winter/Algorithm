'''
1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    1. 바라보는 방향을 유지한 캐로 한 칸을 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다
    2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 있는 경우,
    1. 반시계 방향으로 90도 회전한다
    2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다
    3. 1번으로 돌아간다


d : (0 : 북, 1: 동, 2: 남, 3: 서)
0 : 청소되지 않은 빈 칸
1 : 벽
-1 : 청소된 칸
Q. 로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다

'''

N, M = map(int, input().split())
init_r, init_c, init_d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 4칸 내 청소 가능 구역이 있는가
def is_valid(r, c):
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]

        # 범위 내
        if nr >= N or nr < 0 or nc >= M or nc < 0:
            continue

        if arr[nr][nc] == 0:
            return True
    return False


def set_back_degree(d):
    return (d + 2) % 4


def set_back_pos(r, c, d):
    nd = set_back_degree(d)
    nr = r + dr[nd]
    nc = c + dc[nd]







def bfs():
    answer = 0

    r, c = init_r, init_c
    while True:
        arr[r][c] = -1
        answer += 1

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            # 범위 내
            if nr >= N or nr < 0 or nc >= M or nc < 0:
                continue

            # 벽 or 기청소 구역
            if arr[nr][nc] == 1 or arr[nr][nc] == -1:
                continue

            # 청소 가능 구역 일 때

        # 청소되지 않은 빈 칸이 없는 경우
        # 바라보는 방향을 유지한 채로 후진할 수 있다면 한 칸 후진한다

    # 바라보는 방향의 뒤족 칸이 벽이라 후진할 수 없다면 작동을 멈춘다

    return answer
