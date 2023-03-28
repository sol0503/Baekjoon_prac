import sys
num=int(sys.stdin.readline())

for _ in range(0,num):
  data=input()
  se=list(data)
  sum=0

  for i in se:
    if i == "(":
      sum+=1
    elif i== ")":
      sum-=1
    if sum<0:
      print("NO")
      break
  
  if sum>0:
    print("NO")
  elif sum==0:
    print("YES")