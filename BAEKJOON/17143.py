from pprint import pprint
# R, C <= 100, M <= R*C : 상어의 수
R, C, M = map(int, input().split())
size = [[0 for _ in range(C)] for _ in range(R)]
spe = [[0 for _ in range(C)] for _ in range(R)]
dir = [[0 for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    size[r][c] = z
    spe[r][c] = s
    dir[r][c] = d


answer = 0

# 위, 아래, 오른쪽, 왼쪽
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

# 오른쪽 방향으로 C 만큼 이동한다
for c in range(C):
    # pprint(size)
    # print()
    # 상어가 있는지 찾는다(땅에서 가장 가까운 상어를 잡아야함)
    for r in range(R):
        if size[r][c]:
            answer += size[r][c]
            size[r][c] = 0
            spe[r][c] = 0
            dir[r][c] = 0
            break

    # 상어를 잡은 이후 상어는 움직인다
    visited = [[[] for _ in range(C)] for _ in range(R)]
    for before_r in range(R):
        for before_c in range(C):
            if size[before_r][before_c]:
                speed = spe[before_r][before_c]
                # 최종적으로 위치할 곳
                final_r = before_r
                final_c = before_c
                # 진행방향으로 speed 만큼 이동함
                for s in range(speed):
                    direction = dir[before_r][before_c]
                    nr = final_r + dr[direction]
                    nc = final_c + dc[direction]
                    is_flag = False
                    # 위를 넘어갔을 때 : 아래로 전환
                    if nr < 0:
                        dir[before_r][before_c] = 1
                        is_flag = True
                    # 아래를 넘어갔을 때 : 위로 전환
                    if nr >= R:
                        dir[before_r][before_c] = 0
                        is_flag = True
                    # 오른쪽을 넘어갔을 때 : 왼쪽으로 전환
                    if nc >= C:
                        dir[before_r][before_c] = 3
                        is_flag = True
                    # 왼쪽을 넘어갔을 때 : 오른쪽으로 전환
                    if nc < 0:
                        dir[before_r][before_c] = 2
                        is_flag = True
                    
                    # 방향이 전환됐을 때
                    if is_flag:
                        new_direction = dir[before_r][before_c]
                        nr = final_r + dr[new_direction]
                        nc = final_c + dc[new_direction]
                    # 최종적으로 위치할 곳
                    final_r, final_c = nr, nc
                new_el = (size[before_r][before_c], before_r, before_c)
                visited[final_r][final_c].append(new_el)
    print(visited)
    print()
    for nr in range(R):
        for nc in range(C):
            if visited[nr][nc]:
                # 이동 지점에 두 마리 이상의 상어가 있을 떄
                if len(visited[nr][nc]) >= 2:
                    print('visi', visited[nr][nc])
                    big_r, big_c = 0, 0
                    big_size = -987654321
                    big_spe = 0
                    big_dir = 0
                    for new_pos in visited[nr][nc]:
                        temp_size, before_r, before_c = new_pos
                        if temp_size > big_size:
                            big_size = temp_size
                            big_r = before_r
                            big_c = before_c
                            big_spe = spe[before_r][before_c]
                            big_dir = dir[before_r][before_c]
                        # 새로 이동한 지점의 상어들의 기존값들을 초기화
                        size[before_r][before_c] = 0
                        spe[before_r][before_c] = 0
                        dir[before_r][before_c] = 0
                    size[big_r][big_c] = big_size
                    spe[big_r][big_c] = big_spe
                    dir[big_r][big_c] = big_dir
                # 이동 지점에 한 마리 상어만 있을 때
                else:
                    print('one', visited[nr][nc])
                    # 새로 이동한 영역
                    temp_size, r, c = visited[nr][nc][0]
                    size[nr][nc] = temp_size
                    spe[nr][nc] = spe[r][c]
                    dir[nr][nc] = dir[r][c]
                    # # 기존 영역은 0 으로 초기화
                    size[r][c] = 0
                    spe[r][c] = 0
                    dir[r][c] = 0

print(answer)