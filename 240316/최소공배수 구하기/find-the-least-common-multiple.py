def lcm(n, m):
    result = 0
    for i in range(1,max(n,m)+1): # n번 반복
        if (m % i == 0 and n % i == 0): result = i

    print((n * m) // result)

n, m = map(int, input().split())

lcm(n,m)