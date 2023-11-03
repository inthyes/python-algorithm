B,C,D = map(int,input().split())
a = min(B,C,D)

x = list(map(int,input().split()))
y = list(map(int,input().split()))
z = list(map(int,input().split()))

x.sort(reverse=True)
y.sort(reverse=True)
z.sort(reverse=True)
print(x)

s = 0
for i in range(a):
  s += (x[i]+y[i]+z[i])*0.9

s += sum(x[a::])
s += sum(y[a::])
s += sum(z[a::])

print(sum(x)+sum(y)+sum(z))
print(int(s))