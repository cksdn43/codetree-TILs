import sys

n = int(sys.stdin.readline())

if n >= 3000:
    print('book')
elif n >= 1000:
    print('mask')
elif n >= 500:
    print('pen')
else:
    print('no')