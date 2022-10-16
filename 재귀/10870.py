import sys
def num(n):
  if n==0:
    return 0
  if n==1:
    return 1
  else:
    return num(n-1)+num(n-2)
  
n=int(sys.stdin.readline())

print(num(n))