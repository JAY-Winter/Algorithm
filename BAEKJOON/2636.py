'''
- 판의 가장자리에는 치즈가 놓여져 있지 않다
- 치즈
    하나 이상의 구멍이 있을 수 있다
    공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다

Q) 공기 중에서 치즈가 모두 녹아 없어지는데 걸리는 시간과,
    모두 녹기 한 시간전에 남아있는 치즈조각이 놓여있는 칸의 개수를 구하시오

Sol)
    공기의 위치를 찾는다
    (0,0) 부터 BFS 로 탐색
    모든 공기의 위치를 다시 순회하면서
    사방 탐색으로 치즈가 있으면 녹인다


'''

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def search():
    answer_sec = 0
    answer_cnt = 0
    # 초기 공기 위치
    air_position = []
    while True:
        answer_sec += 1

        # 공기 위치 찾기
        Q = [(0, 0)]

        # 공기 확인 배열
        visited = [[False] * C for _ in range(R)]
        visited[0][0] = True

        while Q:
            r, c = Q.pop(0)
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if R > nr >= 0 and C > nc >= 0 and not visited[nr][nc] and board[nr][nc] == 0:
                    Q.append((nr, nc))
                    visited[nr][nc] = True
                    air_position.append((nr, nc))

        # 공기와 인접한 치즈는 녹음
        melting_cheeses = []
        for air in air_position:
            r, c = air
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if R > nr >= 0 and C > nc >= 0 and board[nr][nc] == 1 and (nr, nc) not in melting_cheeses:
                    melting_cheeses.append((nr, nc))

        if melting_cheeses:
            answer_cnt = len(melting_cheeses)
            for cheese in melting_cheeses:
                r, c = cheese
                board[r][c] = 0
        else:
            return answer_sec - 1, answer_cnt


print(*search())
