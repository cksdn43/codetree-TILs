import sys

n, t = map(int, sys.stdin.readline().split())

cnt = 0

max_cnt = 0

V = list(map(int, sys.stdin.readline().split()))

for v in V:
    if v > t:
        cnt += 1
    elif v <= t:
        cnt = 0
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)