# 변수 선언 및 입력
n = int(input())

tile = {0: []}
cur_location, white, black, gray = 0, 0, 0, 0

# 타일 칠하기
# Black: 0 white: 1 {location: [paint_black, paint_white, last_color] }
for _ in range(n): # T(n)
    move, direct = input().split()
    if direct == 'R':
        value = 0
        step = 1
    else:
        value = 1
        step = -1
    for i in range(1,int(move)): # T(x)
        tile.setdefault(cur_location, []).append(value)
        cur_location += step
    tile.setdefault(cur_location, []).append(value)

# 타일 색 계산
for key in tile.keys(): # T(k)
    if tile[key].count(0) >= 2 and tile[key].count(1) >= 2:
        gray += 1
    elif tile[key][-1] == 0:
        black += 1
    else:
        white += 1

print("{} {} {}".format(white, black, gray))