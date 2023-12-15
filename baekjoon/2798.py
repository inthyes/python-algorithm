n, m = map(int,input().split())
li = list(map(int,input().split()))
nli = []
for i in range(len(li)):
    for j in range(i+1, len(li)):
        for k in range(j+1, len(li)):
            three = li[i] + li[j] + li[k]
            if three > m:
                continue
            else:
                nli.append(three)
print(max(nli))