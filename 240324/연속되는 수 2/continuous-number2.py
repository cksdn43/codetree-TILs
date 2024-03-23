# 변수 선언 및 입력
cnt = 0
max_cnt = 0

N = int(input())
cur_value = int(input())

for i in range(1,N):
    input_value = int(input())
    if cur_value == input_value:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_cnt == cnt
        cnt = 0
        cur_value = input_value

print(max_cnt)