import sys
a=sys.stdin.readline()
c=[]
for i in range(int(a)):
  d=sys.stdin.readline()
  c.append(int(d))

c.sort()
for i in range(int(a)):
  print(c[i])