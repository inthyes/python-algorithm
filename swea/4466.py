t = int(input())
for tc in range(1,t+1):
    x, res = map(int,input().split())
    li = list(map(int,input().split()))
    sum = 0
    li = sorted(li, reverse=True)
    print(li)
    for i in range(res):
        sum += li[i]
    print("#{} {}".format(tc, sum//res))