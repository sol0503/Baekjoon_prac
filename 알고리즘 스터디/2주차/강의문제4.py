import sys
n=int(sys.stdin.readline())
arr=list(map(str,sys.stdin.readline().split()))

x,y=1,1

for i in arr:
    if i=="R":
        y+=1
    elif i=="U":
      if x!=1:
         x-=1
    elif i=="D":
        x+=1
    else:
      if y!=1:
         x-=1#왼쪽의 경우.
print(arr)
print(x,y)