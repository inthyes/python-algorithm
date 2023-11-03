n = input()
li = list(n)
res = []
for i in range(len(n)):
  x = li[i::]
  x = ''.join(map(str, x))
  res.append(x)


res.sort()
for j in res:
  print(j)

