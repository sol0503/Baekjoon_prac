len, wid,he=map(int,input().split())
num=int(input())
arr=[[] for _ in range(num)]
for i in range (num):
    a,b=map(int,input().split())
    arr[a].append(b)


box=len*wid*he
count=0
for i in range (num):
  box1=(2**(num-1-i))**3
  if box>=box1:
      c=box//box1
      print(c)
  else :
    continue

  if c<=int(arr[num-1-i][0]):
    box-=box1*c
    count+=c
  else:
    box-=box1*int(arr[num-1-i][0])
    count+=int(arr[num-1-i][0])
  
  if box==0:
    break

if box!=0:
  print(-1)
else:
  print(count)
