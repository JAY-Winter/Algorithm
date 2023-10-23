N, M = map(int, input().split())

truth_info = list(map(int, input().split()))
if truth_info[0] == 0:
    know_truth = set()
else:
    know_truth = set(truth_info[1:])

parties = []
for _ in range(M):
    party = list(map(int, input().split()))[1:]
    parties.append(set(party))

changed = True
while changed:
    changed = False
    for party in parties:
        if know_truth & party:
            if not know_truth.issuperset(party):
                know_truth = know_truth.union(party)
                changed = True

answer = 0
for party in parties:
    if not know_truth & party:
        answer += 1

print(answer)