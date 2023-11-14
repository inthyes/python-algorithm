t = int(input())
for tc in range(1,t+1):
    a = int(input())
    n = list(map(int,input().split()))
    x = {}
    for i in n:
        if i in x:
            x[i]+=1
        else:
            x[i]= 0
    print("#{} {}".format(tc, max(x, key=x.get)))