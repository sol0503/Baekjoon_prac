a=int(input())
b=a
i=1
while True:
  # if b<10:
  #   x=0
  #   y=b
  # else:
  #   x=b//10
  #   y=b%10
  x=b//10
  y=b%10
  c=(x+y)%10
  num=int(y*10+c)
  if(a==num):
    break
  b=num
  i+=1
print(i)