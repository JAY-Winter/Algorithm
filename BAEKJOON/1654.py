# 만들 수 있는 최대 랜선의 길이를 구하라

# K : 갖고있는 랜선의 개수 <= 1만
# N : 필요한 랜선의 개수 <= 100만
# K <= N
K, M = map(int, input().split())

lans = [int(input()) for _ in range(K)]
print(sorted(lans))
