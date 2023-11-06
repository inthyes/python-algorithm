t = int(input())
for tc in range(1,t+1):
    x = int(input())
    n = input()
    if len(n) % 2 != 0:
        ans = "No"
    else:
        if n[len(n)//2] == n[:len(n)//2]:
            ans = "Yes"
        else:
            ans = "No"
    print("#{} {}".format(tc,ans))