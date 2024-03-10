m1, d1, m2, d2 = map(int, input().split())

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
md = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

idx = 0
if (m1 > m2) or (m1 == m2 and d1 > d2):
    while True:
        if m1 == m2 and d1 == d2:
            break;

        idx -= 1
        d1 -= 1

        if idx <= -7:
            idx = 0
        if d1 <= 0:
            m1 -= 1
            d1 = md[m1]
else:
    while True:
        if m1 == m2 and d1 == d2:
            break;

        idx += 1
        d1 += 1

        if idx >= 7:
            idx = 0
        if md[m1] < d1:
            m1 += 1
            d1 = 1
        
print(days[idx])