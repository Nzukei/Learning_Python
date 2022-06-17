import sys

T = int(sys.stdin.readline())
lstA = []
lstB = []
lst = []

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    lstA.append(A)
    lstB.append(B)
    lst.append(A + B)

for i in range(T):
    print("Case #" + str(i + 1) + ":", lstA[i], '+', lstB[i], '=', lst[i])
