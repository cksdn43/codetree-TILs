a, b, c = map(int, input().split())

day, hour, minute = 11, 11, 11

key = 1
elapsed_minute = 0

if day > a or (day == a and hour > b) or (day == a and hour == b and minute > c):
    key = 0
    elapsed_minute = -1

while key:
    if day == a and hour == b and minute == c:
        break;
    elapsed_minute += 1
    minute += 1

    if minute >= 60:
        hour += 1
        minute = 0
    if hour >= 24:
        day += 1
        hour = 0

print(elapsed_minute)