t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    li1 = list(map(int, input().split()))
    li2 = list(map(int, input().split()))
    a = li2
    b = li1
    c = []
    if len(li1) > len(li2):
        a = li1
        b = li2
        
    for i in range(len(a)+1):
        z = 0
        x = a[i:i + len(b)]
        if len(x) < len(b):
            break
        for j in range(len(b)):
            z += x[j] * b[j]
        c.append(z)
    print(max(c))