N = int(input())
table = [int(input()) for _ in range(N)]
sorted(table)

for i in range(1, N+1):
  x = 0
  if table[i-1] < i:
    print(