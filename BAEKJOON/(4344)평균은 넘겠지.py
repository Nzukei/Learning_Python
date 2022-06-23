import sys

n = int(sys.stdin.readline())

for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    avg = sum(lst[1:]) / lst[0]
    count = 0
    for j in lst[1:]:
        if j > avg:
            count += 1
    rate = count / lst[0] * 100
    print(f'{rate:.3f}%')
