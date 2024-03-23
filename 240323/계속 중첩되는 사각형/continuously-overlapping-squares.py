n = int(input()) - 1

box = {x: [0]*200 for x in range(-100, 101)}
# 첫 사각형 입력 생략
x1, y1, x2, y2 = map(int, input().split())
cur_color, result = 1, 0

# red: 0, blue: 1
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    y1 += 100
    y2 += 100
    for i in range(x1, x2):
        for j in range(y1, y2):
            box[i][j] = cur_color
    cur_color = (cur_color + 1) % 2

for k in box.values():
    result += k.count(1)
print(result)