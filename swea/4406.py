t = int(input())
for tc in range(t):
    li = ['a','e','i','o','u']
    ans = []
    n = input()
    n = list(n)
    print(n)
    for i in n:
        if i not in li:
            ans.append(i)
    ans = ''.join(map(str, ans))
    print("#{} {}".format(tc, ans))