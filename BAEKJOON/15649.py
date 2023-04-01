
# 길이가 M 인 수열
# 1부터 N 까지 자연수 중에서 중복 없이 M 개를 고른 수열

N, M = list(map(int, input().split()))
visited = [False for _ in range(N)]

def dfs(st:str):
    global M
    if len(st) == M:
        for s in st:
            print(s, end=" ")
        print()
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(st + str(i+1))
            visited[i] = False

dfs("")