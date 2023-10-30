N, K = map(int,input().split())
li = []
cnt = 0

for i in range(N):
  x = int(input())
  li.append(x)


for j in reversed(range(N)):
  if K // li[j] >= 1:
    cnt += (K//li[j])
    K %= li[j]

print(cnt)