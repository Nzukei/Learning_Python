import sys

N = int(sys.stdin.readline())

for i in range(N):
    i += 1
    print(' ' * (N - i) + '*' * i)
