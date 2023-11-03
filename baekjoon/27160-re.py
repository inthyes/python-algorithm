n = int(input())
card = {"BANANA","STRAWBERRY","LIME","PLUM"}

for i in range(n):
  fruit, count = map(str,input().split())
  card[fruit] += count

check = 5 in card.values()

if check: print('YES')
else:
  print('NO')