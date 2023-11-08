t = int(input())
for tc in range(t):
    li = list(map(int,input().split()))
    x = sum(li)
    for i in li:
        if i < 40:
            x = x - i + 40
    print("#{} {}".format(tc, x//5))