# 변수 선언 및 입력
n = int(input())

# {location: [paint_black_count, paint_white_count, last_color] }
tile = {0: [0, 0, -1]}
cur_location, white, black, gray = 0, 0, 0, 0

# 도착한 타일 색칠
def coloring():
    global tile, cur_location, color, gray

    if tile[cur_location][2] != 2:
        tile[cur_location][2] = color
        tile[cur_location][color] += 1
        # 회색이 되었는지 확인
        if tile[cur_location][0] >= 2 and tile[cur_location][1] >= 2:
            tile[cur_location][2] = 2
            gray += 1

# 타일 칠하기
# Black: 0 White: 1 Gray: 2
for _ in range(n):
    # 명령어 입력 및 처리
    move, direction = input().split()
    if direction == 'R':
        color, step = 0, 1
    else:
        color, step = 1, -1
    
    for i in range(1,int(move)):
        coloring()
        # 이동
        cur_location += step
        # 처음 도착한 타일 초기화
        if cur_location not in tile:
            tile[cur_location] = [0, 0, -1]
    # 마지막으로 도착한 타일 색칠
    coloring()

# 타일 색 계산
for value in tile.values(): # T(k)
    if value[2] == 0:
        black += 1
    elif value[2] == 1:
        white += 1

print(white, black, gray)