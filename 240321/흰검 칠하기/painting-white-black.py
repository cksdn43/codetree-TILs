# 변수 선언 및 입력
n = int(input())

tile = {0: []}
cur_location = 0

black = 0
gray = 0
white = 0

# 타일 칠하기
# Black: 0 white: 1
for _ in range(n):
    move, direct = input().split()
    if direct == 'R':
        value = 0
        l = 1
    else:
        value = 1
        l = -1
    for i in range(1,int(move)):
        tile.setdefault(cur_location, []).append(value)
        cur_location += l
    tile.setdefault(cur_location, []).append(value)

for key in tile.keys():
    if tile[key].count(0) >= 2 and tile[key].count(1) >= 2:
        gray += 1
    elif tile[key][-1] == 0:
        black += 1
    else:
        white += 1

print("{} {} {}".format(white, black, gray))