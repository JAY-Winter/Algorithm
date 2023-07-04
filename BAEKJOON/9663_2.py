N = int(input())
row_val = [0 for _ in range(N)]
cnt = 0

def is_valid(row):

    for new_row in range(row):
        if row_val[row] == row_val[new_row]:
            return False
        
        elif abs(row - new_row) == abs(row_val[row] - row_val[new_row]):
            return False

    return True

def search(row):
    global cnt
    if row == N:
        cnt += 1
        return
    
    for i in range(N):
        row_val[row] = i    
        if is_valid(row):
            search(row+1)

search(0)
print(cnt)