# 값 입력
m1, d1, m2, d2 = map(int, input().split())
A = input()
# 변수 선언 윤년이기에 2월 29일
day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_days = 0

#  총 날짜 계산
while True:
    if m1 == m2 and d1 == d2:
        break
    total_days += 1
    d1 += 1

    if days[m1] <= d1:
        d1 = 0
        m1 += 1
# A요일이 오는 횟수 계산
# 공식 A요일로 날짜이동 -> A요일 오는 횟수계산 -> A요일도 계산
total_days = (total_days - day_of_week.index(A)) // 7 + 1


print(total_days)