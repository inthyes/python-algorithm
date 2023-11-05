
T = int(input())
for tc in range(1, T + 1):
    p, q, r, s, w = map(int,input().split())
    x = w * p
    if w > r:
        y = q+((w-r)*s)
    else:
        y = q
    print(x, y)
    print("#{} {}".format(tc, min(x,y)))