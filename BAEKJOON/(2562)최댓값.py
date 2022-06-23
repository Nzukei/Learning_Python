import sys

number = [int(sys.stdin.readline()) for _ in range(9)] # 리스트 컴프리헨션

print(max(number))
print(number.index(max(number)) + 1)

# differnt ver.

# import sys
#
# big = int(0)
# pos = int(0)
#
# for i in range(0, 9):
#     push = int(sys.stdin.readline())
#     if big < push:
#         big = push
#         pos = i + 1
#
# print(big)
# print(pos)
