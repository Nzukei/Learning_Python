import sys

T = int(sys.stdin.readline())
case = []

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    case.append(a + b)

for i in range(T):
    print("Case #" + str(i + 1) + ":", case[i])
