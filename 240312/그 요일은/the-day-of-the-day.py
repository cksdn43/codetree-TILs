# 변수 선언 및 입력
m1, d1, m2, d2 = tuple(map(int, input().split()))
A = input()


def num_of_days(m, d):
    # 계산 편의를 위해 월마다 몇 일이 있는지를 적어줍니다. 
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    
    # 1월부터 (m - 1)월 까지는 전부 꽉 채워져 있습니다.
    for i in range(1, m):
        total_days += days[i]
    
    # m월의 경우에는 정확이 d일만 있습니다.
    total_days += d
    
    return total_days


def num_of_day(s):
    # 간단한 비교를 위해 요일을 숫자로 나타내줍니다.
    if s == "Mon": 
        return 0
    elif s == "Tue": 
        return 1
    elif s == "Wed": 
        return 2
    elif s == "Thu": 
        return 3
    elif s == "Fri": 
        return 4
    elif s == "Sat": 
        return 5
    return 6


ans = 0   
start_date = num_of_days(m1, d1)
end_date = num_of_days(m2, d2)
cur_day = num_of_day("Mon")

for date in range(start_date, end_date + 1):
    # 오늘의 요일이 A요일과 같다면 정답에 추가합니다.
    if cur_day == num_of_day(A): 
        ans += 1

    cur_day = (cur_day + 1) % 7

# 출력
print(ans)