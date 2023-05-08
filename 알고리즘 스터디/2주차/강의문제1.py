import sys
n,k=map(int,sys.stdin.readline().split())

count=0
while(n!=1):
  if n<k:
    print(count+(n-1))
    break
  elif n%k==0:
    n=n//k
    count+=1
    if n==1:
      print(count)
  else:
    n-=1
    count+=1
    if n==1:
      print(count)

    

