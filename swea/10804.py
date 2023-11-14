t = int(input())
for tc in range(1, t+1):
    n = input()
    n = n[::-1]

    li = []
    for i in range(len(n)):
        if n[i] == "b":
            li.append("d")
        elif n[i] == "d":
            li.append("b")
        elif n[i] == "p":
            li.append("q")
        elif n[i] == "q":
            li.append("p")
    x = ''.join(map(str, li))
    print("#{} {}".format(tc, x))