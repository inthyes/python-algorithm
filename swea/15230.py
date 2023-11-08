print(ord('a')-97)
# print(ord('b')-97)
t = int(input())
for tc in range(t):
    cnt = 0
    n = input()
    for i in range(len(n)):
        x = ord(n[i])-97
        if x == i:
            if ord(n[i-1])-97 == i -1 or i == 0 and n[i] == 'a':
                cnt+=1
        else:
            break
    print(cnt)
