import sys
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(4)]

for i in range(4):
    print(sum(arr[i]))