# 비어있는 곳 : .
# 물이 차있는 곳 : *
# 돌 : X
# 비버의 굴 : D
# 고슴도치의 위치 : S

# 비버의 굴로 가능한 빨리 도망가야함
# 이동불가능시 "KAKTUS" 출력

# 매 분마다 인접한 네 칸으로 이동 가능
# 물 도 매 분마다 비어있는 칸으로 확장
## 물이 있는 칸과 인접한 비어있는 칸(적어도 한 변을 공유)은 물이 차게 됨

# 고슴도치는 물, 돌 이동 불가능
# 물도 돌, 비버의 소굴로 이동 불가능

# 물이 찰 예쩡인 칸으로 이동 불가능
# 즉, 다음 시간에 물이 찰 예쩡인 칸으로 이동 불가능

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

s = None
b = None
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            s = (i, j)
        elif arr[i][j] == 'D':
            b = (i, j)
from pprint import pprint

def find_water_pos():
    water_pos = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '*':
                water_pos.append((i, j))
    return water_pos

def find_biber_pos():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'S':
                return (i, j)

def find_D():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'D':
                return (i, j)


def is_KAKTUS(biber_pos):
    D_r, D_c = find_D()
    biber_r, biber_c = biber_pos
    if D_r == biber_r and D_c == biber_c:
        return True
    return False


def search(water_list, biber):
    # visited = [[0 for _ in range(C)] for _ in range(R)]
    water_pos_list = find_water_pos()
    biber_r, biber_c = find_biber_pos()
    time = 0
    
    while biber:
        new_water = []
        new_biber = []
        time += 1
        for water_pos in water_pos_list:
            r, c = water_pos
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if nr >= R or nr < 0 or nc >= C or nc < 0:
                    continue
                if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] in ['.', 'S']:
                    arr[nr][nc] = '*'
                    new_water.append((nr, nc))
                # if arr[nr][nc] == 'D' or arr[nr][nc] == 'X' or arr[nr][nc] == 'S':
                #     continue
                # arr[nr][nc] = '*'
                
            # break
            
        for r, c in biber:
            for d in range(4):
                nr = biber_r + dr[d]
                nc = biber_c + dc[d]
                if 0 <= nr < R and 0 <= nc < C and not arr[nr][nc] == '*':
                    if arr[nr][nc] == 'D':
                        return time
                    elif arr[nr][nc] == '.':
                        arr[nr][nc] = 'S'
                        new_biber.append((nr, nc))


                # if nr >= R or nr < 0 or nc >= C or nc < 0:
                #     continue
                # if arr[nr][nc] == '*' or arr[nr][nc] == 'X':
                #     continue
                # if visited[nr][nc]:
                    # continue
                # if arr[nr][nc] == 'D':
                #     return time
                
                # arr[biber_r][biber_c] = '.'
                # arr[nr][nc] = 'S'
                # visited[biber_r][biber_c] = 1
                # biber_r, biber_c = nr, nc
                # Q.append((nr, nc))
                # break

    return 'KAKTUS'

water_list = []
biber = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            water_list.append((i, j))
        elif arr[i][j] == 'S':
            biber.append((i, j))
print(search(water_list, biber))