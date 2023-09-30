'''

- 모든 바이러스는 1번부터 K번까지 바이러스 종류 중 하나

- 바이러스의 증식
    1초마다 증식
    매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식
    증식 과정에서 특정 칸에 이미 어떤 바이러스가 존재한다면, 그곳에는 다른 바이러스 진입 금지

Q) S 초 뒤에 (X, Y) 에 존재하는 바이러스의 종류를 출력하라
만약 바이러스가 존재하지 않는다면, 0 을 출력하라
'''
from collections import deque


def find_init_viruses():
    # 초기 바이러스 위치 찾기
    init_viruses = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                # 행, 열
                init_viruses.append((i, j))
    return init_viruses


def solution(viruses):
    global S, X, Y, K
    # 초기 바이러스를 바이러스 종류로 정렬
    viruses_type_list = [[] for _ in range(K + 1)]
    for viruse in viruses:
        r, c = viruse
        viruse_type = board[r][c]
        viruses_type_list[viruse_type].append((r, c))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    sec = 0

    while True:
        if sec == S:
            return board[X][Y]
        # 바이러스 타입 별로 순회하며 탐색
        for viruse_type, viruses in enumerate(viruses_type_list[:]):
            new_viruses = []
            for viruse in viruses:
                r, c = viruse

                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]

                    if N > nr >= 0 and N > nc >= 0 and board[nr][nc] == 0:
                        board[nr][nc] = viruse_type
                        new_viruses.append((nr, nc))
            viruses_type_list[viruse_type] = new_viruses

        sec += 1


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
X -= 1
Y -= 1

viruses = find_init_viruses()
print(solution(viruses))
