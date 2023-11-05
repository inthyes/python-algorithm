t = int(input())
for tc in range(1,t+1):
    a, b = map(int,input().split())
    if a > 9 or b > 9:
        ans = -1
    else:
        ans = a*b
    print("#{} {}".format(tc, ans))
    