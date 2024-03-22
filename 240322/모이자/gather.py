import sys

INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

min_sum = INT_MAX
for i in range(n):
    sum_diff = 0
    for j in range(n):
        sum_diff += arr[j] * abs(i - j) 

    min_sum = min(min_sum, sum_diff)

print(min_sum)