n = int(input())
cnt = 0
li = ["3", "6", "9"]
for i in range(1, n+1):
    i = list(str(i))
    for j in i:
        if j in li:
            cnt += 1
print(cnt)