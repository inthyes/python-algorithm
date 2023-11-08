a = input()
li = []
for i in range(1, len(a)+1):
    for j in range(len(a)):
        li.append(a[j:i])

setli = set(li)
print(len(setli)-1)