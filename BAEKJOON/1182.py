N, S = map(int, input().split())
nums = list(map(int, input().split()))
selected = [0 for _ in range(N)]
cnt = 0

def search(n, seq, start):
    global cnt
    if n == N+1:
        return
    
    if seq:
        temp_sum = 0
        for s in seq:
            temp_sum += nums[s]
        # print(seq)
        if temp_sum == S:
            cnt += 1
    for i in range(start, N):
        if not selected[i]:
            selected[i] = 1
            search(n+1, seq + [i], i)
            selected[i] = 0

search(0, [], 0)

print(cnt)