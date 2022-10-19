import sys
def money(a,b,c):
  if b>=c:
    return -1
  else:
    d=int(a/(c-b)+1)
    return d
    
a,b,c=map(int,sys.stdin.readline().split())
print(money(a,b,c))