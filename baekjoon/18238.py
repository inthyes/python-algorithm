N = list(input())
c = 0
first = 'A'
for i in N:
  left = ord(i) - ord(first)
  right = ord(first) - ord(i)

  if left < 0:
    left += 26
  elif right < 0:
    right += 26

  c +=min(left,right)
  first = i
print(c)
  