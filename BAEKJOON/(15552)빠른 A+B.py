import sys

T = int(sys.stdin.readline())
add = []
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    add.append(A + B)

for i in range(T):
    print(add[i])
