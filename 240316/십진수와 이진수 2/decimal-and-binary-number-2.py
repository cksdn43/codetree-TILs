# 변수 선언 및 입력
N = list(input())
L = len(N)
result = 0

for i in range(L):
    result += int(N[-i-1]) * 2**i
# 십진수변환에 17곱
result *= 17
# 리스트재활용
N.clear()
while result >= 1:
    N.append(result % 2)
    result //= 2

# 이진수 출력
for i in N[::-1]:
    print(i, end='')