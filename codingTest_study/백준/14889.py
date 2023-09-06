def dfs(c):
  global sum1
  t1, t2 = 0, 0
  if len(s) == n // 2 and s[0] == 0:
    for i in range(n):
      if i not in s:
        k.append(i)
   #  print(s,k)
    for i in range(len(s)):
      for j in range(i + 1, len(s)):
        t1 += a[s[i]][s[j]]+ a[s[j]][s[i]]
        t2 += a[k[i]][k[j]]+a[k[j]][k[i]]

    sum1 = min(sum1, abs(t1 - t2))
    k.clear()
    return

  for i in range(c, n):
    if i not in s:
      s.append(i)
      dfs(i)
      s.pop()


n = int(input())
a = []
for i in range(n):
  a.append(list(map(int, input().split())))
s = []
k = []
sum1 =999999999

dfs(0)

print(sum1)
