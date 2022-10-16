import sys
def num(n):
  count=0
  if n%5==0:
    return n/5
  if n/5!=0:
    a=int(n/5)
    for i in reversed(range(a+1)):
      b=int(n-5*i)
      if b%3==0:
        return (i+b/3)
  if n%3==0:
    return n/3
  return -1

a=int(sys.stdin.readline())
print(int(num(a)))
    
    
