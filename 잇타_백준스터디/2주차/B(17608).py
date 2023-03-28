import sys
num=int(sys.stdin.readline())
arr=[]
for i in range(0,num):
    a=int(sys.stdin.readline())
    arr.append(a)
arr.reverse()

count=1
min=arr[0]
for i in range(1,num):
    if arr[i]>min:
      count+=1
      min=arr[i]


print(count)