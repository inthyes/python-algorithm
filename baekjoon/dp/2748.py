import sys
n = int(sys.stdin.readline())

f = [i for i in range(n+1)]
print(f)
for i in range(2, n+1):
  f[i] = f[i-1]+f[i-2]
  print(f[i])
print(f[-1])