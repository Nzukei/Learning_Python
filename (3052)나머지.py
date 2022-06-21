import sys

lst = [0 for _ in range(1000)] # 리스트 컴프리헨션
cnt = 0

for i in range(10):
    tmp = int(sys.stdin.readline())
    lst[tmp % 42] += 1

for i in range(1000):
    if lst[i] >= 1:
        cnt += 1

print(cnt)
