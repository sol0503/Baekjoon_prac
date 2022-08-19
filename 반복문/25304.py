total=int(input())
count=int(input())
sum=0
for i in range(1,count+1):
  a,b=map(int,input().split())
  sum+=a*b

if sum==total:
  print("Yes")
else:
  print("No")