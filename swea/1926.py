n = int(input())
x = [3,6,9]
cnt = 0
for i in range(1,n+1):
  for j in range(i):
    if j in [3,6,9]:
      cnt += 1
  if cnt == 0:
    print(i,end=" ")
  else:
    print("-"*i,end=" ")