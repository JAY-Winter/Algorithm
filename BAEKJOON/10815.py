# 숫자카드 N 개
# 정수 M 개
# 이 수가 적혀있는 숫자카드를 가지고 있는지 유무 판단

# 갖고있는 카드 개수
N = int(input()) 
# 갖고있는 숫자 카드에 적혀있는 리스트(1 ~ 500,000)
has_cards = list(map(int, input().split()))
has_cards.sort()
M = int(input())
# 갖고있는지 판단해야하는 리스트(1 ~ 500,000)
is_cards = list(map(int, input().split()))

# is_cards 를 순회하면서 has_cards 에 포함되어있는지 확인하기
def search(target, arr):
    N = len(arr)
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

answer = []
for card in is_cards:
    result = search(card, has_cards)
    answer.append(result)

print(*answer)        
    

