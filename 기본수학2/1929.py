import sys
def count(i):
  if i==1:
    return False
  else:
    for k in range(2,int(i**0.5)+1):
      if i%k==0:
        return False
    return True

a=list(map(int,sys.stdin.readline().split()))
for i in range(a[0],a[1]+1):
  if count(i):
    print(i)