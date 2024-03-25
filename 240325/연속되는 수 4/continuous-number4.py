import sys
N = int(sys.stdin.readline())

# up: 0, down: 1
state = 0
cnt = 1
max_cnt = 1
pre_value = int(sys.stdin.readline())

for _ in range(N-1):
    cur_value = int(sys.stdin.readline())
    if cur_value > pre_value and state == 0:
        cnt += 1
    elif cur_value < pre_value and state == 0:
        cnt = 2
        state = 1
    elif cur_value < pre_value and state == 1:
        cnt += 1
    elif cur_value > pre_value and state == 1:
        cnt = 2
        state = 0
    if cnt > max_cnt:
        max_cnt = cnt
    
    pre_value = cur_value

print(max_cnt)