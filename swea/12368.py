T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  x, y = map(int,input().split())
  z = 0
  if x + y > 24:
        z = x+y // 24
  else:
        if x + y == 24:
            z = 0
        else:
            z = x + y
  print("#{} {}".format(test_case,z))