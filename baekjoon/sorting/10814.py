n = int(input())
li = []
for _ in range(n):
  li.append(list(input().split()))

li.sort(key=lambda a:int(a[0]))

for i in range(n):
  print(li[i][0],li[i])