import sys
N = int(sys.stdin.readline())
li = []
for i in range(N):
  x = int(sys.stdin.readline())
  li.append(x)

y = sorted(li)

for i in range(N):
  print(y[i])