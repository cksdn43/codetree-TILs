def gcd(n, m):
    result = 1

    for i in range(1,max(n,m)):
        if (m % i == 0 and n % i == 0): result = i

    return result

n, m = map(int, input().split())

print(gcd(n, m))