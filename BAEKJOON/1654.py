'''
갖고있는 K 개의 랜선은 길이가 제각각이다
랜선을 모두 N 개의 같은 길이의 랜선으로 만들고 싶었기 때문에
K개의 랜서을 잘라서 만들어야한다

Q) 최대 랜선의 길이를 구하라

'''

# 만들 수 있는 최대 랜선의 길이를 구하라

# K : 갖고있는 랜선의 개수 <= 1만
# N : 필요한 랜선의 개수 <= 100만
# K <= N
K, M = map(int, input().split())

lans = [int(input()) for _ in range(K)]


start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2

    total = sum([cable // mid for cable in lans])

    if (total >= M):
        start = mid + 1
    else:
        end = mid - 1

print(end)
