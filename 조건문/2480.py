a,b,c=map(int,input().split())
if(a==b):
  if(b==c):
    print(1000*a+10000)
  else:
    print(100*a+1000)
elif(b==c):
  print(100*b+1000)
elif(a==c):
  print(100*a+1000)
else:
  m=max(a,b,c)
  print(m*100)
  