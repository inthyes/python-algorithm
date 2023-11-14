n = int(input())

li = ["3","6","9"]

for i in range(1,n+1):
    cnt = 0
    i = str(i)
    # print(i)
    for j in range(len(i)):
        if i[j] in li:
            cnt+= 1
    if cnt == 0:
        print(i, end=" ")
    else:
        print("-"*cnt, end= " ")