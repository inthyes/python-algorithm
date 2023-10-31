n = int(input())
A = []
for nc in range(n):
  a = list(map(int,input().split()))
  A.append(a)

# 정렬
A.sort(key=lambda x:x[0])
total = 0
# n만큼 반복
for i in range(n):
  if total >= A[i][0]:
    total += A[i][1]
  else:
    total = A[i][0]+A[i][1]

print(total)