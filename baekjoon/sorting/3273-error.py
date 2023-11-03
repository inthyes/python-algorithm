import sys

N = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
o = int(sys.stdin.readline())
cnt = 0

for i in range(N):
  for j in range(N):
    if i != j and li[i] + li[j] == o:
        cnt += 1

print(cnt//2)