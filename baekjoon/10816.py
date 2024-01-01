import sys
input = sys.stdin.readline
n = int(input())
res = list(map(int,input().split()))
dicRes = {}
for i in res:
    if i in dicRes:
        dicRes[i] += 1
    else:
        dicRes[i] = 1

m = int(input())
ans = list(map(int, input().split()))

for i in ans:
    if i in dicRes:
        print(dicRes[i], end = " ")
    else:
        print(0, end = " ")