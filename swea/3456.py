t = int(input())
for tc in range(1,t+1):
    li = list(map(int,input().split()))
    if li[1] == li[2]:
        ans = li[0]
    else:
        if li[1] == li[0]:
            ans = li[2]
        else:
            ans = li[1]
    print("#{} {}".format(tc, ans))