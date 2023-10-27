T = int(input())
for test_case in range(1, T + 1):
    li = [50000,10000,5000,1000,500,100,50,10]
    N = int(input())
    print("#{}".format(test_case))
    for i in range(len(li)):
        print(N//li[i],end = " ")
        N %= li[i]
        print()