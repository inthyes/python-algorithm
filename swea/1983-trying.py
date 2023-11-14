t = int(input())
n, k = map(int, input().split())
Sum = []
for i in range(n):
    x, y, z = map(int,input().split())
    Sum.append(x * 0.35 + y * 0.45 + z * 0.2)

# print(sorted(Sum, reverse = True)[k])