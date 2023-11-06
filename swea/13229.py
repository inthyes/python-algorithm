t = int(input())
for tc in range(1,t+1):
    li = ["SAT","FRI","THU","WED","TUE","MON", "SUN"]
    x = input()
    for i in range(len(li)):
        if x == li[i]:
            print("#{} {}".format(tc, i+1))