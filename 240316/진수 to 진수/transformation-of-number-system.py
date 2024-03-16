# 변수 선언 및 입력
a, b = map(int, input().split())
n = list(input())
L = len(n)
result = 0

# a진수로 변환
for i in range(L):
    result += int(n[-i-1]) * a**i

# 리스트재활용
n.clear()

# b진수로 변환
while result >= 1:
    n.append(result % b)
    result //= b

# 결과 출력
for i in n[::-1]:
    print(i, end='')