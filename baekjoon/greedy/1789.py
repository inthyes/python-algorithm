import sys
S = int(input())
t = list(map(int,sys.stdin.readline().split()))
t.sort(reverse=True)
t1 = []
z = 1
for i in t:
  t1.append(i+z)
  z += 1
print(max(t1)+1)
  