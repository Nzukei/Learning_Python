import sys

n = int(sys.stdin.readline())   # 첫째 줄에 시험 본 과목의 개수 n
lst = []

test = list(map(float, sys.stdin.readline().split()))   # 모든 시험 성적들

for i in range(n):
    average = test[i] / max(test) * 100
    lst.append(average)

print(sum(lst) / n)
