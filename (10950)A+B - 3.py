T = int(input())
add = []

for i in range(T):
    A, B = map(int, input().split())
    add.append(A + B)

for i in range(T):
    print(add[i])
