'''
Q. 아기 상어가 엄마 사엉에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력하라

- 가장 처음에 상어의 크기는 2
- 자신의 크기와 같은 수의 물고리를 먹을 때 마다 크기가 1씩 증가
    크기가 2일 때는 2마리 먹어야 1 증가
- 1초에 상하좌우로 이동

- 지나갈 수 있는 조건
    1. 자신의 크기보다 작아야함
    2. 자신의 크기와 같아야함

- 먹을 수 있는 조건
    1. 자신의 크기보다 작은 물고기만 가능

- 이동 결정 방법
    - 더 이상 먹을 수 있는 물고기가 공간에 없다면 엄마에게 도움 요청
    - 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹음
    - 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기
        - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기
        - 가장 왼쪽에 있는 물고기

- 칸
    - 0 : 빈 칸
    - 1 ~ 6 : 물고기의 크기
    - 9 : 상어의 위치
    - N <= 20

Sol)
1. 아기 상어의 위치를 찾는다
2. 현재 위치에서 먹을 수 있는 상어를 찾는다
    - 이동 결정 방법 참고
3. 먹을 수 있는 상어가 있을 때, 상어를 먹는다
    이때, 크기가 M 이면 M 마리를 먹어야 크기가 1 증가함
'''

from collections import deque


def find_baby_shark_position():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return i, j


def calculate_distance(r, c, size):
    global N
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    distance_arr = [[-1] * N for _ in range(N)]
    distance_arr[r][c] = 0
    Q = deque([(r, c)])
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 좌표 내 & 아직 방문하지 않은 곳 & 현재 사이즈보다 작거나 같은 곳
            if N > nr >= 0 and N > nc >= 0 and distance_arr[nr][nc] == -1 and size >= arr[nr][nc]:
                distance_arr[nr][nc] = distance_arr[r][c] + 1
                Q.append((nr, nc))
    return distance_arr


# 먹을 수 있는 상어 위치와 거리를 반환
def find_can_eat_every_shark(size, distance_arr):
    which_can_ate = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] < size and arr[i][j] != 0:
                distance = distance_arr[i][j]
                if distance != -1:
                    which_can_ate.append((i, j, distance))
    return which_can_ate


def find_can_eat_specific_shark(which_can_ate):
    if len(which_can_ate) == 1:
        specific_shark = which_can_ate[0]
    else:
        # 거리가 가장 가까운 물고기 > 가장 위에 있는 물고기 > 가장 왼쪽에 있는 물고기
        specific_shark = sorted(which_can_ate, key=lambda x: (x[2], x[0], x[1]))[0]
    return specific_shark


def eat_shark(r, c):
    arr[r][c] = 0
    return


def main():
    cur_size = 2
    cur_eat_cnt = 0
    total_sec = 0
    init_shark_r, init_shark_c = find_baby_shark_position()
    arr[init_shark_r][init_shark_c] = 0
    while True:
        # 현재 상어의 사이즈와 위치를 기반으로 지나갈 수 있는 모든 좌표에 대한 거리를 포함한 리스트
        distance_arr = calculate_distance(init_shark_r, init_shark_c, cur_size)
        # 현재 상어의 사이즈를 기반으로 먹을 수 있는 모든 상어의 좌표와 거리를 포함한 리스트
        which_can_eat = find_can_eat_every_shark(cur_size, distance_arr)

        # 더 이상 먹을 수 있는 물고기가 공간에 없다는 뜻
        if not which_can_eat:
            return total_sec
        # 먹을 수 있는 모든 상어 중 "이동결정방법"에 따라 분류된 한 마리의 상어
        specific_shark = find_can_eat_specific_shark(which_can_eat)
        # 한 마리의 상어를 먹음

        eat_shark(specific_shark[0], specific_shark[1])
        cur_eat_cnt += 1

        total_sec += specific_shark[2]

        init_shark_r, init_shark_c = specific_shark[0], specific_shark[1]
        # 지금까지 먹었던 상어의 마리 수가 현재 사이즈와 같을 시
        if cur_eat_cnt == cur_size:
            cur_size += 1
            cur_eat_cnt = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = main()
print(answer)

