t = int(input())
for tc in range(1,t+1):
    n = int(input())
    li = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n-1):
        if li[i] != max(li) and li[i] != min(li):
            cnt += 1
            print(li[i])
    print("#{} {}".format(tc, cnt))