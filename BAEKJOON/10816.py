N = int(input())
cards = list(map(int, input().split()))
M = int(input())
search_cards = list(map(int, input().split()))

def search(target: int, cards: list[int]):
    start, end = 0, len(cards)-1
    cnt = 0
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == target:
            cnt += 1
            start = mid + 1
        elif cards[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return cnt

cards.sort()
answer = []
for card in search_cards:
    result = search(card, cards)
    answer.append(result)
print(*answer)