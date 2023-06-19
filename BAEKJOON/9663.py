N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

# print(arr)

def validate(arr):
    # 상 하 좌 우 상좌 상우 하우 하좌
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, 1, -1]
    L = len(arr)
    for i in range(L):
        for j in range(L):
            if arr[i][j] == 1:
                for d in range(8):
                    for e in range(1, L+1):
                        nr = i + (dr[d]*e)
                        nc = j + (dc[d]*e)
                        if L > nr >= 0 and L > nc >= 0 and arr[nr][nc] == 1:
                            return False
    return True

selected = [0 for _ in range(N)]
cnt = 0

cols = [0 for _ in range(N)]

def is_validate(row):
    for new_row in range(row):
        # 1. 같은 열에 위치해있는지
        if cols[row] == cols[new_row]:
            return False
        # 2. 대각선에 있는지
        elif abs(cols[row] - cols[new_row]) == abs(row - new_row):
            return False
    return True

def search(row):
    global cnt
    if row == N:
        cnt += 1
        return
    
    for i in range(N):
        cols[row] = i
        
        if is_validate(row):
            search(row+1)

search(0)
print(cnt)