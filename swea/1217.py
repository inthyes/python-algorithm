
for tc in range(1,11):
    t = int(input())
    n, m = map(int,input().split())
    x = 1
    for i in range(m):
        x *= n
    print("#{} {}".format(tc, x))