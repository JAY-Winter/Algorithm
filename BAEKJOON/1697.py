# N <= 10만
# K <= 10만

# 걷다 : X-1 or X+1
# 순간이동 : 2*X

# N : 수빈이가 있는 위치
# K : 동생이 있는 위치

# 5-10-9-18-17

# 5 6 7 8 9 10 11 12 13 14 15 16 17
N, K = map(int, input().split())
START = 0
END = 100001
distance = [0 for _ in range(END)]

def bfs():
    Q = [N]
    
    while Q:
        pos = Q.pop(0)
        if pos == K:
            print(distance[pos])
            return
        
        for next_pos in (pos-1, pos+1, pos*2):
            if START <= next_pos < END and not distance[next_pos]:
                distance[next_pos] = distance[pos] + 1
                Q.append(next_pos)

bfs()