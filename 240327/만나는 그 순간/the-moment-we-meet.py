import sys
# 변수 선언 및 입력
N, M = map(int, sys.stdin.readline().split())

result = -1
time = 0
cur_location = 0

# key == time, value == location
A = {}
B = {}

#A 시간 당 위치 계산
for i in range(1,N + 1):
    direct, step = sys.stdin.readline().split()
    step = int(step)
    while (step > 0):
        time += 1
        step -= 1
        if direct == 'R':
            cur_location += 1
            A[time] = cur_location
        else:
            cur_location -= 1
            A[time] = cur_location

# 초기화
time = 0
cur_location = 0

#B 시간 당 위치 계산 만약 A랑 같은 시간이 있으면 중단
for i in range(1,M + 1):
    direct, step = sys.stdin.readline().split()
    step = int(step)
    while (step > 0):
        time += 1
        step -= 1
        if direct == 'R':
            cur_location += 1
            B[time] = cur_location
        else:
            cur_location -= 1
            B[time] = cur_location
        if A[time] == B[time]:
            result = time
            break
    if result == time:
        break

print(result)