t = int(input())
for tc in range(1,t+1):
    x = input()
    print("#{}".format(tc),end = " ")
    for i in range(len(x.split())):
        print(x.split()[i][0].upper(),end = "")