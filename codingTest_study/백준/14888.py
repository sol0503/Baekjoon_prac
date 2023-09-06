def dfs(c, tmp):
  global min1, max1
  if c == n:
    max1 = max(max1, tmp)
    min1 = min(min1, tmp)
  else:
    if arr2[0] > 0:
      arr2[0] -= 1
      dfs(c + 1, tmp + arr1[c])
      arr2[0] += 1
    if arr2[1] > 0:
      arr2[1] -= 1
      dfs(c + 1, tmp - arr1[c])
      arr2[1] += 1
    if arr2[2] > 0:
      arr2[2] -= 1
      dfs(c + 1, tmp * arr1[c])
      arr2[2] += 1
    if arr2[3] > 0:
      arr2[3] -= 1
      dfs(c + 1, int(tmp / arr1[c]))
      arr2[3] += 1


n = int(input())
max1 = -10000000000
min1 = 10000000000

arr1= list(map(int, input().split()))
arr2= list(map(int, input().split()))
dfs(1, arr1[0])
print(max1)
print(min1)
