import sys

min_sum = sys.maxsize

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    sum_diff = 0
    for j in range(n):
        sum_diff += arr[j] * abs(i - j) 

    min_sum = min(min_sum, sum_diff)

print(min_sum)