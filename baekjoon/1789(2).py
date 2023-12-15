import sys
n = int(sys.stdin.readline())
res = 0
cnt =0 
for i in range(1,n+1):
  res += i
  cnt += 1
  if res > n:
    cnt -= 1
    break
print(cnt)