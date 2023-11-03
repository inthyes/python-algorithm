import sys
n = int(sys.stdin.readline())
li = []
for i in range(n):
  li.append(sys.stdin.readline().strip())

li = list(set(li))
li.sort()
li.sort(key=len)
print(li)
# for j in range(n):
#   print(li[j])