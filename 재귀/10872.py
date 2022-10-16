import sys
def num(a):
  if a==1 or a==0:
    return 1
  else:
    return a*num(a-1)

a=int(sys.stdin.readline())

print(num(a))

