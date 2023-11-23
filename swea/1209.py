for tc in range(10):
    t = int(input())

    x = []
    s = 0
    for _ in range(100):
        x.append(list(map(int,input().split())))

    TSum = []
    for i in range(100):
        aSum = 0
        bSum = 0
        for j in range(100):
            aSum += x[i][j]
            bSum += x[j][i]
        TSum.append(aSum)
        TSum.append(bSum)

    for i in range(100):
        cSum = 0
        dSum = 0
        cSum += x[i][i]
        dSum += x[i][99-i]
        TSum.append(cSum)
        TSum.append(dSum)
    print("#{} {}".format(t, max(TSum)))

