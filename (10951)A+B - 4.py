import sys

while True: #1 available instead of True
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except:
        break
