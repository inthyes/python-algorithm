t = int(input())
for tc in range(t):
    s = input()
    n = list(map(int, list(s)))
    x = []
    for i in range(1, len(n)):
        a = int(''.join(map(str,n[:i])))
        b = int(''.join(map(str,n[i:])))
        x.append(a+b)
    print(min(x))
