t = int(input())
for tc in range(1,t+1):
    x = 0
    n = int(input())
    for i in range(1,10):
        if n % i == 0 and n // i < 10:
            x += 1
    print("#{} {}".format(tc, 'Yes' if x > 0 else 'No'))
