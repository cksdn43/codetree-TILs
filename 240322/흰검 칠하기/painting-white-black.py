# 변수 선언 및 입력
n = int(input())

tile = {0: [0, 0, -1]}
cur_location, white, black, gray = 0, 0, 0, 0


# 타일 칠하기
# Black: 0 White: 1 Gray: 2
# {location: [paint_black_count, paint_white_count, last_color] }
for _ in range(n): # T(n)
    # 명령어 입력 및 처리
    move, direct = input().split()
    if direct == 'R':
        color, step = 0, 1
    else:
        color, step = 1, -1
    
    for _ in range(1,int(move)): # T(x)
        # 처음 도착한 타일 초기화
        if cur_location not in tile:
            tile[cur_location] = [0, 0, -1]
        # 타일 색칠
        if tile[cur_location][2] != 2:
            tile[cur_location][2] = color
            tile[cur_location][color] += 1
            if tile[cur_location][0] >= 2 and tile[cur_location][1] >= 2:
                tile[cur_location][2] = 2
        cur_location += step

    # 도착한 타일 색칠  
    if cur_location not in tile:
        tile[cur_location] = [0, 0, -1]
    if tile[cur_location][2] != 2:
        tile[cur_location][2] = color
        tile[cur_location][color] += 1
        if tile[cur_location][0] >= 2 and tile[cur_location][1] >= 2:
            tile[cur_location][2] = 2

# 타일 색 계산
for key in tile.keys(): # T(k)
    if tile[key][2] == 2:
        gray += 1
    elif tile[key][2] == 0:
        black += 1
    else:
        white += 1

print(white, black, gray)