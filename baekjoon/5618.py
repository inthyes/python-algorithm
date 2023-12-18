import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

for i in range(1, min(li)+1):
    cnt = 0
    for j in li:
        if j % i == 0:
            cnt += 1
    if cnt == len(li):
        print(i)