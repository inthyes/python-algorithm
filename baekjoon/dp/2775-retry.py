t = int(input())
for tc in range(t):
  # 층수
  floor = int(input())
  # 호수
  ho = int(input())
  # 0층 나열(1부터 입력받은 호까지)
  F0 = [x for x in range(1,ho+1)]
  for k in range(floor):
    for i in range(1,ho):
      F0[i] += F0[i-1]
  print(F0[-1])