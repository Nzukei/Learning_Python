import sys

N = int(sys.stdin.readline()); num = N; cnt = 0
while True:
    add_num = sum(map(int, str(num)))
    new_num = ((num % 10) * 10) + (add_num % 10)
    cnt += 1
    if new_num == N:
        break
    num = new_num
print(cnt)
