import sys
stu=int(sys.stdin.readline())
a=[]
a.insert(0,1)
arr=[]
arr=list(map(int,sys.stdin.readline().split()))
for i in range(0,stu):
  if i==0:
    continue
  else:
    if arr[i]==0:
      a.insert(i,i+1)
    else:
      a.insert(i-arr[i],i+1)

for i in a:
  print(i,end=' ')