import sys
num=int(sys.stdin.readline())
# if num==0:
#     count=0
#     print(count)
# elif num==1 | num==2:
#     count=1
#     print(count)
# else:
arr=[]
for i in range(0,num+1):
  if i==0:
    arr.insert(i,0)
  elif i==1:
    arr.insert(i,1)
  else:
    arr.insert(i,arr[i-1]+arr[i-2])
print(arr[num])