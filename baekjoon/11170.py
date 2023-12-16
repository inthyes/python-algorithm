t = int(input())
for _ in range(1, t+1):
    cnt = 0
    n, m = list(map(int,input().split()))
    for i in range(n, m+1):
        cnt += str(i).count("0")
    print(cnt)


