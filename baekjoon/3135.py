a, b = map(int,input().split())
n = int(input())
li = []
ans = []
x = 0
for i in range(n):
  li.append(int(input()))

for j in li:
  if abs(a-b) > abs(j-b):
    ans.append(abs(j-b) + 1)
  else:
    ans.append(abs(a-b))
print(min(ans))
