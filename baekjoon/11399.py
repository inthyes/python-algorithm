N = int(input())
li = list(map(int,input().split()))
li = sorted(li)
li2 = []
for i in range(N):
  if i == 0:
    li2.append(li[i])
  else:
    li2.append(li[i] + li2[i-1])
print(sum(li2))
  