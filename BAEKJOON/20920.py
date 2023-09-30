'''
단어의 우선 순위
1. 자주 나오는 단어일 수록 앞
2. 해당 단어의 길이가 길수록 앞
3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞

길이가 M 이상인 단어들만 확인

1 <= N <= 100,000
1 <= M <= 10

Q. 단어장의 앞에 위치한 단어부터 한 줄에 하나씩 출력하라
'''
import sys

word_dict = {}
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    word = input()

    if len(word) < M:
        continue

    if word_dict.get(word):
        word_dict[word][0] += 1
    else:
        word_dict[word] = [1, len(word), word]

sorted_word_dict = sorted(word_dict.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))

for word in sorted_word_dict:
    print(word[0])
