import sys

a,b=map(int,sys.stdin.readline().split())
arr1=[]
arr2=[]

for i in range(a):
  row1=list(map(int,sys.stdin.readline().split()))
  arr1.append(row1)

for i in range(a):
  row2=list(map(int,sys.stdin.readline().split()))
  arr2.append(row2)

for i in range(a):
  for j in range(b):
    arr1[i][j]+=arr2[i][j]
    print(arr1[i][j],end=" ")
  print()
  





