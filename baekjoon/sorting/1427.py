import sys
n = int(sys.stdin.readline())
li = list(map(int, str(n)))
li.sort(reverse=True)
print("".join(map(str,li)))