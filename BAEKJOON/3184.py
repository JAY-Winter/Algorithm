from pprint import pprint
'''
. : 빈 필드
# : 울타리
o : 양
v : 늑대

울타리를 지나지 않고 다른 칸으로 이동할 수 있다면
두 칸은 같은 영역 안에 속대힜다

영역 안의 양의 수가 늑대의 수보다 많으면 이기고
늑대를 우리에서 쫓아낸다
그렇지 않다면 늑대가 그 지역 안의 모든 양을 먹는다

'''

# R: 행
# C :열
R, C = map(int, input().split())
maps = [list(input().strip()) for _ in range(R)]

visited = [[0 for _ in range(C) ] for _ in range(R)]


def search(r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    Q = [(r, c)]
    wolfs = 0
    sheeps = 1
    wolfs_pos = []
    sheeps_pos = [(r, c)]
    while Q:
        r, c = Q.pop(0)
        visited[r][c] = 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if nr >= R or nr < 0 or nc >= C or nc < 0:
                continue

            if maps[nr][nc] == '#':
                continue
            
            if visited[nr][nc]:
                continue

            if maps[nr][nc] == 'v':
                wolfs += 1
                wolfs_pos.append((nr, nc))
            
            if maps[nr][nc] == 'o':
                sheeps += 1
                sheeps_pos.append((nr, nc))

            Q.append((nr, nc))
    
    if sheeps > wolfs:
        print('양이 더 많음', sheeps, wolfs)
        for wolf_pos in wolfs_pos:
            r, c = wolf_pos
            maps[r][c] = '.'
    else:
        print('늑대가 더 많음', sheeps, wolfs)
        for sheep_pos in sheeps_pos:
            r, c = sheep_pos
            maps[r][c] = '.'

pprint(maps)
for r in range(R):
    for c in range(C):
        if maps[r][c] == 'o':
            search(r, c)


sheeps, wolfs = 0, 0

for r in range(R):
    for c in range(C):
        if maps[r][c] == 'o':
            sheeps += 1
        
        elif maps[r][c] == 'v':
            wolfs += 1

print(sheeps, wolfs)