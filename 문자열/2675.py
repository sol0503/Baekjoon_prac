import sys
num= int(sys.stdin.readline())
for i in range (num):
  sum=""
  a,b=input().split()
  for j in b:
    # for k in range (0,int(a)):
      sum+=j*int(a)
  print(sum)
  