N = list(input())
L = len(N)
result = 0

for i in range(L):
    result += int(N[-i-1]) * 2**i

result *= 17
N.clear()
while result >= 1:
    N.append(result % 2)
    result //= 2
N.reverse()

for i in N:
    print(i, end='')