t = int(input())
for tc in range(1,t+1):
    n = input()
    a = ''
    for i in n:
        if n.count(i) != 0 and n.count(i) % 2 == 0:
            a += i
            x = ''.join(sorted(a))
    if a == '':
        x = 'Good'
    print("#{} {}".format(tc, x))
