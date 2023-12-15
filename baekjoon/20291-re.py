n = int(input())
ans = {}
for i in range(n):
  i = input().split('.')[1]
  if i not in ans:
    ans[i] = 1
  else:
    ans[i] += 1

res = list(ans.keys())
res.sort()
for j in res:
  print(j, ans[j])

