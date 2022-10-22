import sys
a=int(sys.stdin.readline())
c=[]
def find(n):
  if n==1:
    return
  for i in range(2,n+1):
    if n%i ==0:
      c.append(i)
      d=int(n/i)
      find(d)
      break
    if n==i:
      c.append(n)


  
find(a)
c=sorted(c)
for i in c:
  print(i)


