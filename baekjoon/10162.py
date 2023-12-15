N = int(input())
li = [300,60,10]
if N % 10 != 0:
  print(-1)
else:
  for i in range(len(li)):
    print(N//li[i],end=" ")
    N%=li[i]
