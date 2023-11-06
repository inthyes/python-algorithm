t = int(input())
for tc in range(1,t+1):
    n = int(input())
    li = list(map(int,input().split()))
    avg = sum(li) // n
    cnt = 0
    for i in li:
        if i <= avg:
            cnt += 1
    print("#{} {}".format(tc, cnt))