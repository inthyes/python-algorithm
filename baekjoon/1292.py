x, y = map(int,input().split())
li = [] * len(y)
for i in range(1,y+1):
    for j in range(i):
        li.append(j)