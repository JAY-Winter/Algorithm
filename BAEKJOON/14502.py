# 연구소에 벽을 세워야함
# 벽을 3개 세워야함
# 0 : 빈 칸
# 1 : 벽
# 2 : 바이러스
# 바이러스는 1(벽) 못 지나감
# 벽을 3개 세운 후, 바이러스가 다 퍼진 상황에서 퍼질 수 없는 공간을 안전 영역이라고함
from pprint import pprint

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
answer = -987654321

# pos : 바이러스의 위치
def virus(new_maps, pos):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0 , -1, 1]

    r, c = pos
    Q = [(r, c)]
    while Q:
        r, c = Q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 바이러스가 퍼질 수 있는 새로운 좌표 조건
            if N > nr >= 0 and M > nc >= 0 and new_maps[nr][nc] == 0:
                new_maps[nr][nc] = 2
                Q.append((nr, nc))

def check(maps):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                cnt += 1
    return cnt

def set_maps(n, start):
    global answer
    # 벽의 개수가 3개 일때 체크
    if n == 3:
        # 체크할 때마다 새로운 배열 생성
        new_maps = [row[:] for row in maps]
        # 모든 좌표를 순회하며 바이러스일 때 전파 수행
        for i in range(N):
            for j in range(M):
                if maps[i][j] == 2:
                    pos = (i, j)
                    virus(new_maps, pos)
        # 전파가 끝났을 때 안전 영역 체크
        safe_arr_cnt = check(new_maps)
        if safe_arr_cnt > answer:
            answer = safe_arr_cnt
        return

    for i in range(start, N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                set_maps(n+1, i)
                maps[i][j] = 0

n, start = 0, 0
set_maps(n, start)

print(answer)