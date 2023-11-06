t = int(input())
for tc in range(1,t+1):
    word = input()
    for i in range(len(word)//2):
        if word[i] == word[-1-i]:
            answer = 1
        else:
            answer = 0
    print("#{} {}".format(tc,answer))