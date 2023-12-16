m = int(input())
n = int(input())
i = m
li = []
while i <= n:
    if int(i ** 0.5) ** 2 == i:
        li.append(i)
    i += 1
if not li:
    print(-1)
else:
    print(sum(li))
    print(min(li))



