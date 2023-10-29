N = int(input())
li = list(map(int,input().split()))
c = 0
for i in range(N):
    if li[i] == c % 3:
        c+=1
print(c)

