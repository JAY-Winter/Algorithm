# from collections import deque

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

# # 1 육지


# # 육지 찾기


# def find_land(arr, selected):

#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#     for r in range(N):
#         for c in range(N):
#             if arr[r][c] == 1 and not selected[r][c]:
#                 temp_lands = set()
#                 Q = deque([(r, c)])
#                 while Q:
#                     r, c = Q.popleft()
#                     selected[r][c] = 1
#                     temp_lands.add((r, c))
#                     for d in range(4):
#                         nr = r + dr[d]
#                         nc = c + dc[d]
#                         if N > nr >= 0 and N > nc >= 0 and not selected[nr][nc]:
#                             Q.append((nr ,nc))
#     if temp_lands:
#         return temp_lands
#     else:
#         return None


# selected = [[0 for _ in range(N)] for _ in range(N)]

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# lands_list = []
# for r in range(N):
#     for c in range(N):
#         if arr[r][c] == 1 and not selected[r][c]:
#             temp_lands = set()
#             Q = deque([(r, c)])
#             while Q:
#                 r, c = Q.popleft()
#                 selected[r][c] = 1
#                 temp_lands.add((r, c))
#                 for d in range(4):
#                     nr = r + dr[d]
#                     nc = c + dc[d]
#                     if N > nr >= 0 and N > nc >= 0 and not selected[nr][nc] and arr[nr][nc] != 0:
#                         Q.append((nr ,nc))
#                         temp_lands.add((nr, nc))

#             lands_list.append(temp_lands)


# def cal_distance(land1, land2):
#     global answer
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]

#     for temp_land in land1:
#         s_r, s_c = temp_land
#         for temp_land2 in land2:
#             e_r, e_c = temp_land2
#             visited = [[0 for _ in range(N)] for _ in range(N)]
#             cnt = 0
#             Q = deque([(s_r, s_c, cnt)])
#             while Q:
#                 r, c, cnt = Q.popleft()
#                 visited[r][c] = 1
#                 for d in range(4):
#                     nr = r + dr[d]
#                     nc = c + dc[d]
                    
#                     if N > nr >= 0 and N > nc >= 0 and not visited[nr][nc]:
#                         if nr == e_r and nc == e_c:
#                             if cnt < answer:
#                                 answer = cnt
#                         else:
#                             Q.append((nr, nc, cnt+1))




# L = len(lands_list)
# answer = 987654321
# for i in range(L-1):
#     for j in range(i+1, L):
#         cal_distance(lands_list[i], lands_list[j])

# print(answer)

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
selected = [[0 for _ in range(N)] for _ in range(N)]

Q = deque()
islands = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0

# 섬 구획 정하기
for i in range(N):
    for j in range(N):
        if arr[i][j] and not selected[i][j]:
            cnt += 1
            Q.append((i, j))
            selected[i][j] = True
            islands[i][j] = cnt

            while Q:
                r, c = Q.popleft()
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if N > nr >= 0 and N > nc >= 0 and not selected[nr][nc] and arr[nr][nc]:
                        Q.append((nr, nc))
                        selected[nr][nc] = True
                        islands[nr][nc] = cnt

# 섬 개수 세기
island_cnt = 0
for line in islands:
    for land in line:
        if land > 0:
            island_cnt += 1



answer = float('inf')

for i in range(island_cnt):
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    Q = deque()
    for r in range(N):
        for c in range(N):
            if islands[r][c] == i + 1:
                Q.append((r, c))
                dist[r][c] = 0
    
    # 반복문 당 Q: 섬 구획별 좌표들
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 좌표 내 일 때
            if N > nr >= 0 and N > nc >= 0:
                # 섬 그리고 지금 Q 에 들어와있지 않은 섬일 때 계산
                if islands[nr][nc] and islands[nr][nc] != i + 1:
                    answer = min(answer, dist[r][c])
                    break
                # 섬이아님 그리고 아직 방문안 한 곳일 때
                if not islands[nr][nc] and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    Q.append((nr, nc))

print(answer)
