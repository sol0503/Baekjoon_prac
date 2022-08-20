def d(n):
  n=n+sum(map(int,str(n)))
  return n

list_num=set()

for i in range(1,10001):
  list_num.add(d(i))

for i in range(1,10001):
  if i not in list_num:
    print(i)