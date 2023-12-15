N = int(input())
x = list(map(int,input().split()))

li = sorted(x, reverse= True)
li2 = sorted(x)

res = []
for i in range(N):
  a = li[i]+li2[i]
  res.append(a)

print(min(res))
