from pprint import pprint

R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

# 내부를 2로 바꿔잉 ㅋ
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def set_air_zone(r=0, c=0):
    visited = [[False] * C for _ in range(R)]
    visited[r][c] = True
    Q = [(r, c)]
    graph[r][c] = 2
    while Q:
        r, c = Q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if R > nr >= 0 and C > nc >= 0 and not visited[nr][nc] and (graph[nr][nc] == 0 or graph[nr][nc] == 2):
                visited[nr][nc] = True
                graph[nr][nc] = 2
                Q.append((nr, nc))

def is_disapear(r, c):
    zero_cnt = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if R > nr >= 0 and C > nc >= 0 and graph[nr][nc] == 2:
            zero_cnt += 1
    if zero_cnt >= 2:
        return True
    return False


def get_disapear_list():
    disapear_list = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 1 and is_disapear(i, j):
                disapear_list.append((i, j))
    return disapear_list


def disapear(disapear_list):
    for disapear_cheese in disapear_list:
        r, c = disapear_cheese
        graph[r][c] = 2


def is_done(graph):
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 1:
                return True
    return False


sec = 0
while is_done(graph):
    sec += 1
    set_air_zone(0, 0)
    disapear_list = get_disapear_list()
    disapear(disapear_list)

print(sec)