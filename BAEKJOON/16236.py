# 최초 아기 상어 크기 2
# 상어는 1초에 상하좌우 인접한 한 칸씩 이동

# 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다
# 자신의 크기보다 작은 물고기만 먹을 수 있다
# 크기가 같은 물고기는 먹을 수 없지만 지나갈 수 있다
# 물고기를 먹으면 그 칸은 빈 칸이 된다
# 물고기를 먹으면 크기가 1 씩 증가한다

# 더 이상 먹을 수 있는 물고기가 공간에 없다면 도움 요청
# 먹을 수 있는 물고기가 1 마리라면 그 물고기를 먹음
# 먹을 수 있는 물고기가 1 마리 보다 많다면, 거리가 가장 가까운 물고기를 먹음
## 거리는 최솟값
## 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기

# 출력
# 몇 초 동안 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 지 구하라

# 0: 빈칸
# 1 ~ 6 : 물고기 크기
# 9 : 아기상어위치

"""
1. 전체 칸을 순회하며 먹을 수 있는 물고기가 있는지 확인
2-1. 먹을 수 있는 물고기가 있을 때
3-1. 먹을 수 있는 물고기가 1마리일 때
3-2. 먹을 수 있는 물고기가 1마리 이상일 때
2-2. 먹을 수 있는 물고기가 없을 때 : 종료

별도의 함수: 현재 상어 위치에서 먹을 수 있는 물고기의 위치 거리(지나야 하는 칸의 개수) 구하기

"""


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
size = 2
sec = 0

def can_eat(size):
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and size > arr[i][j]:
                return True
    return False

def how_many_can_eat(size):
    cnt = 0
    pos_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and size > arr[i][j]:
                cnt += 1
                new_pos = (i, j)
                pos_list.append(new_pos)
    return (cnt, pos_list)

def cal_distance(now_pos, search_pos_list):
    print('cal_distance',now_pos, search_pos_list)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    distance_list = []

    for search_pos in search_pos_list:
        r, c = now_pos
        distance = 0
        Q = [(r, c, distance)]
        visited = [[0] * N for _ in range(N)]
        while Q:
            r, c, distance = Q.pop(0)
            visited[r][c] = 1
            now_pos = (r, c)

            if now_pos == search_pos:
                break
            
            for d in range(4):
                new_r = r + dr[d]
                new_c = c + dc[d]

                if new_r >= N or new_r < 0 or new_c >= N or new_c < 0:
                    continue
                if visited[new_r][new_c]:
                    continue
                if arr[new_r][new_c] > size:
                    continue
                
                Q.append((new_r, new_c, distance+1))

        distance_list.append((distance, search_pos))
    return distance_list

def check_start_pos():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                return (i, j)

def eat(pos):
    r, c = pos
    arr[r][c] = 0
    return


# main 실행
start_pos = check_start_pos()
while can_eat(size):
    can_eat_cnt, can_eat_pos_list = how_many_can_eat(size)

    if can_eat_cnt == 1:
        distance = cal_distance(start_pos, can_eat_pos_list)
        print('distance', distance)
        eat_pos = can_eat_pos_list[0][1]
        r = eat_pos[0]
        c = eat_pos[1]
        arr[r][c] = 0
        size += 1
        print(size)
    elif can_eat_cnt > 1:
        print('한 마리 이상 먹을 수 있음')
        distance = cal_distance(start_pos, can_eat_pos_list)
        print('distance', distance)
        sorted_distance = sorted(distance, key=lambda x: (x[0], x[1][0], x[1][1], print(x[1][0], x[1][1])))
        print('sorted_distance', sorted_distance)
        eat_pos = sorted_distance[0][1]
        print('eat_pos', eat_pos)
        r = eat_pos[0]
        c = eat_pos[1]
        arr[r][c] = 0
        size += 1
