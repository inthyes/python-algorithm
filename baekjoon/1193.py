n = int(input())
a, b = 1, 1
for i in range(1,n):
  if a == b:
    b += 1
  elif a < b:
    a += 1
    b -= 1
  elif a > b:
    a -= 1
    b += 1

  
print("{}/{}".format(a,b))