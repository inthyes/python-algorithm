t = int(input())
for tc in range(1,t+1):
    n = int(input())
    nli = list(map(int, str(n)))
    nli = set(nli)
    print("#{} {}".format(tc, len(nli)))