t = int(input())
for tc in range(1,t+1):
    n = int(input())
    print("#{}".format(tc),end = " ")
    for i in range(1,n+1):
        print("{}/{}".format(i,n),end = " ")
    print()