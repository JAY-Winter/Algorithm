import sys
sys.setrecursionlimit(10000)

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
normal_visited = [[False] * N for _ in range(N)]
color_visited = [[False] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0 , 0, - 1, 1]

normal_count = 0
color_count = 0

def dfs(is_normal, color, r, c):
    if is_normal and normal_visited[r][c]:
        return
    if not is_normal and color_visited[r][c]:
        return

    if is_normal:
        normal_visited[r][c] = True
    else:
        color_visited[r][c] = True

    for d in range(4):
        new_r = r + dr[d]
        new_c = c + dc[d]

        if new_r >= N or new_r < 0 or new_c >= N or new_c < 0:
            continue

        new_color = arr[new_r][new_c]

        if is_normal:
            if color != new_color:
                continue
            dfs(is_normal, color, new_r, new_c)
        else:
            if (color == 'B' and new_color != 'B') or (color != 'B' and new_color == 'B'):
                continue
            dfs(is_normal, color, new_r, new_c)
        

for i in range(N):
    for j in range(N):
        color = arr[i][j]

        if not normal_visited[i][j]:
            normal_count += 1
            dfs(True, color, i, j)

        if not color_visited[i][j]:
            color_count += 1
            dfs(False, color, i, j)

print(normal_count, color_count)