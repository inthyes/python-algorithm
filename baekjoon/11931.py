n = int(input())
x = []
for _ in range(n):
  x.append(int(input()))

x.sort(reverse=True)

for i in x:
  print(i)