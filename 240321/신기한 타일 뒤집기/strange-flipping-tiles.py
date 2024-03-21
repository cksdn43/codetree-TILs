# 변수 선언 및 입력
n = int(input())

tile = {0: []}
cur_location, white, black = 0, 0, 0

# 타일 칠하기
# Black: 0 white: 1
for _ in range(n): # T(n)
    move, direct = input().split()
    if direct == 'R':
        value = 0
        l = 1
    else:
        value = 1
        l = -1
    for i in range(1,int(move)): # T(x) x is move
        tile[cur_location] = value
        cur_location += l
    tile[cur_location] = value

# 타일 색 계산
for key in tile.keys(): # T(k) k is location
    if tile[key] == 0:
        black += 1
    else:
        white += 1

# 결과 출력
print("{} {}".format(white, black))

#time complexity O(nx)