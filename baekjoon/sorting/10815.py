import sys

n = int(sys.stdin.readline())
x = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
y = list(map(int,sys.stdin.readline().split()))

res = {}
for i in range(n):
    res[x[i]] = 0

for j in range(m):
    if y[j] not in res:
        print(0, end=" ")
    else:
        print(1, end=" ")
