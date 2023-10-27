T = int(input())
for tc in range(T):
  N = int(input())
  li = [25,10,5,1]
  for i in range(len(li)):
    print(N//li[i],end = " ")
    N %= li[i]