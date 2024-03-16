# n, m의 최대공약수를 반환합니다.
def gcd(n, m):
    result = 1
    for i in range(1,max(n,m)+1): # n번 반복
        if (m % i == 0 and n % i == 0): result = i

    return result

# 변수 입력
n, m = map(int, input().split())

# 결과 출력
print(gcd(n, m))

# 2n + 1