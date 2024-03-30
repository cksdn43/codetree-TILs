import sys

a = int(sys.stdin.readline())

if(a%2 != 0):
    a += 3
if (a%3 == 0):
    a //= 3
print(a)