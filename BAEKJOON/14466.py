'''
- 정사각형 N*N (2 ~ 100) 격자
- 인접한 목초지 사이는 일반적으로 자유롭게 건너갈 수 있지만, 그 중 일부는 길을 건너야 한다.
- 격자 바깥으로는 이동 불가

- K 마리 소(K <=100, K<= N^2) 소가 격자에 있고,
    각 소는 서로 다른 목초지에 있다

- 어떤 두 소는 길을 건너지 않으면 만나지 못 할 수가 있다. -> 이때, 이런 소가 몇 쌍인지 세어보자
'''


def dfs(r, c, cow, reachable, visited):
    # 격자를 벗어나거나 길로만 가야하는 좌표거나 이미 방문한 좌표인 경우
    if not (N > r >= 0 and N > c >= 0) or visited[r][c]:
        return

    # 현재 위치 방문
    visited[r][c] = True
    # 탐색을 시작한 소가 방문할 수 있는 위치 값에 추가
    reachable[cow].add((r, c))

    # 상하좌우
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        # 이동하려는 목초지 사이에 길이 없는 경우에만 탐색
        if not road_map.get((r, c, nr, nc), True):
            continue
        dfs(nr, nc, cow, reachable, visited)


N, K, R = map(int, input().split())

roads = []
for _ in range(R):
    road = list(map(lambda x: x - 1, list(map(int, input().split()))))
    roads.append(road)

cows = []
for _ in range(K):
    cow_r, cow_c = map(lambda x: x - 1, map(int, input().split()))
    cows.append((cow_r, cow_c))

# 길을 건너야 하는 좌표
road_map = {}
for r1, c1, r2, c2 in roads:
    road_map[(r1, c1, r2, c2)] = False
    road_map[(r2, c2, r1, c1)] = False

# 각 소마다 도달할 수 있는 좌표
reachable = [set() for _ in range(K)]

# 모든 소를 탐색
for cow_number, (r, c) in enumerate(cows):
    visited = [[False] * N for _ in range(N)]
    dfs(r, c, cow_number, reachable, visited)

# 길을 건너지 않고 만날 수 없는 소의 쌍 계산
isolated_pairs = 0
for i in range(K):
    for j in range(i + 1, K):
        # 공통된 집합이 없을 시
        # -> reachable : 각 소들이 도달할 수 있는 모든 좌표 집합
        # -> 교집합 : 두 소가 공통적으로 도달할 수 있는 좌표 집합
        if not reachable[i].intersection(reachable[j]):
            isolated_pairs += 1

print(isolated_pairs)
