import sys
num=int(sys.stdin.readline())
count=0
a=0
b=0
c=0
d=0
e=0
f=0

for s in range(0,59):
  s=str(s)
  if "3" in s:
    b+=1

count=b

for m in range(0,59):
  m=str(m)
  if "3" in m:
    f+=60
    a+=1

count=f+(60-a)*count

for i in range(0,num):
  i=str(i)
  if "3" in i:
    d+=60*60
    e+=1
count=d+(num-e+1)*count

print(count)