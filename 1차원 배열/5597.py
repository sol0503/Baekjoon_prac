import sys
arr=[]
for i in range(0,5):
  a= int(sys.stdin.readline())
  arr.append(a)
arr=sorted(arr)
k=0
n=0
for i in range(1,8):
  if arr[n]!=i:
    print(arr[n])
    k+=1
    if k==2:
      break
  else:
    n+=1


