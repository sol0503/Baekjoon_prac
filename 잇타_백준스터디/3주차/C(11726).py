import sys
num=int(sys.stdin.readline())
arr=[]
arr.append(0)
for i in range(1,num+1):
  if i==1:
    arr.insert(i,1)
  elif i==2:
    arr.insert(i,2)
  else:
    arr.insert(i,arr[i-1]+arr[i-2])

print(arr[num]%10007)