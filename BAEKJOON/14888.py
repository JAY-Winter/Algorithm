N = int(input())
A = list(map(int, input().split()))
plus, minus, mul, div = list(map(int, input().split()))
operator = []

if plus:
    for _ in range(plus):
        operator.append('+')

if minus:
    for _ in range(minus):
        operator.append('-')

if mul:
    for _ in range(mul):
        operator.append('*')

if div:
    for _ in range(div):
        operator.append('//')

operator_cnt = N-1

def cal(temp):
    stack = []
    for el in temp:
        # 비어있으면 넣음
        if not stack:
            stack.append(el)
        # 비어있지 않을 때
        else:
            # 숫자가 아니면 넣음
            if el not in range(1, 101):
                stack.append(el)
            # 숫자일 때
            else:
                op = stack.pop()
                num = stack.pop()
                if op == '+':
                    new_num = num + el
                elif op == '-':
                    new_num = num - el
                elif op == '*':
                    new_num = num * el
                elif op == '//':
                    if num < 0 and el > 0:
                        num *= (-1)
                        new_num = (num // el) * (-1)
                    else:
                        new_num = num // el
                stack.append(new_num)
    return stack.pop()

selected = [0 for _ in range(operator_cnt)]
cals = []
def recur(n, seq):
    if n == operator_cnt:
        temp = []
        for idx, num in enumerate(A):
            temp.append(num)
            if idx < len(A)-1:
                temp.append(operator[seq[idx]])
        cals.append(cal(temp))

    for i in range(operator_cnt):
        if not selected[i]:
            selected[i] = 1
            recur(n+1, seq + [i])
            selected[i] = 0
recur(0, [])

print(max(cals))
print(min(cals))

