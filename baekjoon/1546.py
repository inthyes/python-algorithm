N = int(input())
li = list(map(int,input().split()))
M = max(li)
for i in range(N):
  li[i] = li[i]/M*100
print(sum(li)/N)