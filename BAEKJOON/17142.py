'''
0 : 빈칸
1 : 벽
2 : 비활성 바이러스

비활성 바이러스 M 개를 활성 바이러스로 변경한다
활성 바이러스는 1초마다 상하좌우로 퍼짐

1. 비활성화 바이러스 리스트 중에서 M 개씩 뽑는다
2. M 개씩 뽑은 바이러스 를 갖고 bfs 를 돌린다
3. bfs 돌릴 때의 값 을 비교한다


Q. 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다
안 될 경우에는 -1 을 출력한다
'''
from pprint import pprint

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def get_viruses():
    viruses = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                viruses.append((i, j))
    return viruses


viruses = get_viruses()

vistied = [False] * len(viruses)


def bfs(arr, init_viruses):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    Q = init_viruses
    print(Q)
    visited = [[False] * N for _ in range(N)]
    sec = 0
    while Q:
        sec += 1
        r, c = Q.pop(0)
        visited[r][c] = True
        arr[r][c] = '*'

        next_Q = []
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if N > nr >= 0 and N > nc >= 0 and not visited[nr][nc] and (arr[nr][nc] == 0 or arr[nr][nc] == 2):
                next_Q.append((nr, nc))
                visited[nr][nc] = True
                arr[nr][nc] = '*'
        Q = next_Q

    pprint(arr)
    print(sec)
    print()


def main(n, c, viruses, checked):
    # M 개 뽑음
    if n == M:
        new_arr = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                new_arr[i][j] = arr[i][j]

        init_viruses = []
        for check in checked:
            r, c = viruses[check]
            init_viruses.append((r, c))
        bfs(arr=new_arr, init_viruses=init_viruses)

        return

    for i in range(c, len(viruses)):
        if not vistied[i]:
            vistied[i] = True
            main(n + 1, i, viruses, checked + [i])
            vistied[i] = False


main(0, 0, viruses, [])
