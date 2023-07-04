# N : 갖고 있는 카드 개수 <= 50만개
N = int(input())
# 갖고 있는 카드들
cards = sorted(list(map(int, input().split())))

# M <= 50만개
M = int(input()) 
# 이 카드들로 내가 갖고있는 카드가 몇 개 인지 확인해야함
find_cards = list(map(int, input().split()))

# 완전 탐색하게되면 50^2 이 됨(N^2)
# 이분탐색으로 풀어보자

answer = []

for card in find_cards:
    cnt = 0
    left = 0
    right = N
    
    while left < right:
        mid = (left + right) // 2
        if card == cards[mid]:
            cnt = cards[left:right].count(card)
            break
        if card > cards[mid]:
            left = mid + 1
        else:
            right = mid
    answer.append(cnt)

print(answer)

