import sys

n = int(sys.stdin.readline())

for i in range(n):
    case = map(str, sys.stdin.readline())
    score = 0
    count = 0
    for j in list(case):
        if j == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)
