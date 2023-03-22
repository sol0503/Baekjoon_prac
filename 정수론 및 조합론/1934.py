import sys
a=int(input())
for i in range(a):
  x,y=map(int,input().split())
  if x==1:
    print(y)
  elif y==1:
    print(x)
  elif x==y:
    print(x)
  else:
    if x>y:
      tmp=x
      x=y
      y=tmp
    i=1
    while x>=i:
      t=[]
      if x%i==0:
        t.append(i)
      i+=1
    t.sort(reverse=True)
    for k in t:
      if y%k==0:
        print(y*(x/k))
        break

