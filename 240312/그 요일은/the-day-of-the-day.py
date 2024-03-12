m1, d1, m2, d2 = map(int, input().split())
A = input()

day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_days = 0

while True:
    if m1 == m2 and d1 == d2:
        break
    total_days += 1
    d1 += 1

    if days[m1] <= d1:
        d1 = 0
        m1 += 1

total_days = (total_days - day_of_week.index(A)) // 7


print(total_days + 1)