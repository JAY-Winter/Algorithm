# 같은 1x1크기의 칸에 여러 개의 나무가 심어져있을 수도 있다
# 가장 처음에 양분은 모든 칸에 5만큼 들어있다

# 봄 : 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다
# - 각각의 나무는 1x1크기의 칸에 있는 양분만 먹을 수 있다
# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다
# 만약, 땅에 양분이 부족해 자신의 나이만큼 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다

# 여름 : 봄에 죽은 나무가 양분으로 변한다.
# - 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다, 소수점 아래는 버린다

# 가을 : 나무가 번식한다
# - 번식하는 나무는 나이가 5의 배수이어야 하며
# - 인접한 8개의 칸에 나이가 1인 나무가 생긴다

# 겨울 : 땅에 양분을 추가한다
# - 각 칸에 추가되는 양분으 양은 A[r][c] 이고, 입력으로 주어진다

# Q: K 년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하시오

# N : NxN 크기의 땅 N <= 10
# M : M 개의 나무 M <= N^2
# K : K 년 K<=1000
N, M, K = map(int, input().split())
# A : 겨울에 각 땅에 추가되는 땅의 양분
A = [list(map(int, input().split())) for _ in range(N)]

# 초기 양분값
vals = [[5 for _ in range(N)] for _ in range(N)]


# 상도가 심은 나무의 위치와 해당 나무의 나이
plants_age = [[[] for _ in range(N)] for _ in range(N)]

# 심는 나무의 위치와 나이 입력받기
for _ in range(M):
    # (x, y) : 나무의 위치, z : 해당 나무의 나이
    x, y, z= map(int, input().split())
    x -= 1
    y -= 1

    plants_age[x][y].append(z)

def spring():
    dead_pos = []
    # 나무가 자신의 나이만큼 양분을 먹는다
    # 나이가 1 증가한다
    for r in range(N):
        for c in range(N):
            # 해당 위치에 나무가 존재할 때
            if plants_age[r][c]:
                min_age = 0
                min_r, min_c = 0, 0
                min_idx = 0
                # 해당 위치에 나무가 여러개 존재할 때, 나이가 어린 나무부터 양분을 먹는다
                if len(plants_age[r][c]) > 1:
                    # 나이가 어린 양분의 위치와 나이를 찾는다
                    min_age = 987654321
                    min_r, min_c = 0, 0
                    for idx, plant in enumerate(plants_age[r][c]):
                        age = plant
                        if age < min_age:
                            min_age = age
                            min_r, min_c = r, c
                            min_idx = idx
                # 해당 위치에 나무가 1개만 존재할 때
                else:
                    min_r, min_c = r, c
                    min_age = plants_age[min_r][min_c][0]
                    min_idx = 0
                # 만약 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없으면 해당 나무는 즉시 죽는다
                if vals[min_r][min_c] < min_age:
                    dead_pos.append((min_r, min_c, min_age))
                    min_idx = plants_age[min_r][min_c].index(min_age)
                    plants_age[min_r][min_c].pop(min_idx)
                else:
                    # 양분을 먹는다
                    vals[min_r][min_c] -= min_age
                    # 나이가 1 증가한다
                    plants_age[min_r][min_c][min_idx] += 1
    return dead_pos

def summer(dead_pos):
    for pos in dead_pos:
        r, c, age = pos
        vals[r][c] += age // 2

def autumn():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    can_breed_pos = []
    for r in range(N):
        for c in range(N):
            # 나무가 존재할 때
            if plants_age[r][c]:
                # 나무가 있고 나무의 나이가 5의 배수일 때
                for plant in plants_age[r][c]:
                    if plant % 5 == 0:
                        can_breed_pos.append((r, c))
                        break

    # 인접한 8개의 칸에 나이가 1인 나무가 생긴다
    if can_breed_pos:
        for breed_pos in can_breed_pos:
            r, c = breed_pos
            visited[r][c] = 1
            dr = [-1, -1, -1, 0, 0, 1, 1, 1]
            dc = [-1, 0, 1, -1, 1, -1, 0, 1]
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if nr >= N or nr < 0 or nc >= N or nc < 0:
                    continue

                # if visited[r][c]:
                #     continue
                
                plants_age[nr][nc].append(1)

def winter():
    for r in range(N):
        for c in range(N):
            vals[r][c] += A[r][c]

def find_alive_plants():
    alive_plants = 0
    for r in range(N):
        for c in range(N):
            alive_plants += len(plants_age[r][c])
    return alive_plants


# K 년 만큼 진행
for _ in range(K):
    # 봄
    dead_pos = spring()

    # 여름
    if dead_pos:
        summer(dead_pos)

    # 가을 
    autumn()

    # 겨울
    winter()

alive_plants = find_alive_plants()
print(alive_plants)