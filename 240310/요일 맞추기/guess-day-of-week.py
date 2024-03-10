m1, d1, m2, d2 = map(int, input().split())

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

idx = 0
while True:
    if m1 == m2 and d1 == d2:
        break;

    idx -= 1
    d2 += 1

    if idx <= -6:
        idx = 0
    if md[m2] < d2:
        m2 += 1
        d2 = 1

print(days[idx])