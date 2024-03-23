# 변수 선언 및 입력
key, cnt = -1, 0
max_cnt = 1


N = int(input())

# 최장 연속 부분 수열 계산
for i in range(N):
    input_value = int(input())
    if (input_value < 0 and key < 0) or (input_value > 0 and key > 0):
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 1
        key *= -1
if cnt > max_cnt:
    max_cnt = cnt

print(max_cnt)