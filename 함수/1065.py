import sys


def hansu (n):
  sum=0
  for i in range(1,n+1):
    if i<10:
      sum+=1
    elif i<100:
      sum+=1
    elif i<1000:
      a=int(i/100)
      b=int((i%100)/10)
      c=(i%100)%10
      x=int(a-b)
      y=int(b-c)
      if x==y:
        sum+=1
  print(sum)

n=int(sys.stdin.readline())
hansu(n)

