from sys import stdin
a, b = map(int,stdin.readline().split())
A = set(map(int,stdin.readline().split()))
B = set(map(int,stdin.readline().split()))

res = A - B

if res:
    print(len(res))
    print(*sorted(list(res)))
else:
    print(0)