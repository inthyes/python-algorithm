x = 1000
y = int(input())
li =[500,100,50,10,1]
z = 1000-y
a = 0
for i in li:
    z %= li[i]
    a += 1
print(a)