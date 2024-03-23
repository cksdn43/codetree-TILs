# 변수 선언 및 입력
cnt = 1
max_cnt = 1

N = int(input())
cur_value = int(input())

# 최장 연속 부분 수열 계산
for i in range(1,N):
    input_value = int(input())
    if cur_value == input_value:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 1
        cur_value = input_value

print(max_cnt)