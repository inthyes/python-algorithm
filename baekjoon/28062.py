N = int(input())
li = list(map(int,input().split()))
s = sorted(li)

for i in range(N,1):
    if sum(li) % 2!= 0:
        li = li.remove(i)
        
    else:
        break
if sum(li) % 2 == 0:
    print(0)
else:
    print(sum(li))
