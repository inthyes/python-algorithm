N = int(input())
M = int(input())
A = []

for i in range(N,M+1):
  if i == 1:
    continue
  err =0 
  for j in range(2,i):
    if i % j == 0:
      err += 1
  if err == 0:
    A.append(i)

if not A:
  print(-1)
else:
  print(sum(A))
  print(min(A))