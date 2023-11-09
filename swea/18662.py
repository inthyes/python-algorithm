t = int(input())
for tc in range(t):
    a,b,c = map(int,input().split())
    if b - a == c - b:
        ans = 0.0
    else:
        x = (a+c) / 2
        ans = abs(x - b)
    print("#{} {}".format(tc, ans))