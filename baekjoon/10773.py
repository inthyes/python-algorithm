n = int(input())
li = []
for i in range(n):
    x = int(input())
    if x == 0:
        li.pop()
    else:
        li.append(x)

if len(li) == 0:
    print(0)
else:
    print(sum(li))