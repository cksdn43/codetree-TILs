def gcd(n, m):
    result = 0

    for i in range(1,n):
        if (m % i == 0 and n % i == 0): result = i

    return result

n, m = map(int, input().split())

print(gcd(n, m))