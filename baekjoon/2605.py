n = int(input())
li = list(map(int, input().split()))
res = []
for i in range(n):
    if li[i] == 0:
        res.insert(0, i+1)
    else:
        res.insert(li[i], i+1)

for i in reversed(res):
    print(i, end = " ")