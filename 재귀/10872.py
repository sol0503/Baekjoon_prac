import sys
a=int(sys.stdin.readline())
b=1
if a>=1:
  for i in range(1,a+1):
    b*=i

print(b)
