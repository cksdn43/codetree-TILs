A = input()
cnt = 0

for a in range(len(A)):
    if A[a] == '(':
        for b in range(a, len(A)):
            if A[b] == ')':
                cnt += 1

print(cnt)