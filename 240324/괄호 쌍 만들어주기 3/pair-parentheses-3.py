# 변수 선언 및 입력
A = input()
n = len(A)
cnt = 0

# 반복문을 돌며 괄호 쌍 계산
for a in range(n):
    if A[a] == '(':
        for b in range(a, n):
            if A[b] == ')':
                cnt += 1

print(cnt)