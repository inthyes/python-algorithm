t = int(input())
for tc in range(t):
    x = input()
    if x.count('x') > 8:
        ans = "NO"
    else:
        ans = "YES"
    print(ans)