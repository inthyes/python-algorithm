t = int(input())
for tc in range(1,t+1):
    n = list(input())
    setN = set(n)
    ans = "Yes"
    for i in setN:
        if n.count(i) != 2:
            ans = "No"
    print(ans)