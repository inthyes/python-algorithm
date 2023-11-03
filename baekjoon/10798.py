x=[]
for _ in range(5):
  x.append(input())

print(x)

for i in range(5):
  x[i] = [char for char in x[i]]
print(x)
