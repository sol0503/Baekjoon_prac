import sys

a=int(sys.stdin.readline())
b=set(map(int,sys.stdin.readline().split()))
c=int(sys.stdin.readline())
d=list(map(int,sys.stdin.readline().split()))
for i in range(c):
  if d[i] in b:
    print(1,end=" ")
  else:
    print(0,end=" ")