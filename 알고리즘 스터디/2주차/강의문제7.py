n=input()

n=list(n)
count=0
arr=[]
for i in n:
  i=int(ord(i))
  if  48<=i and i<=57:
    count+=int(chr(i))
  else:
    arr.append(chr(i))

arr.sort()
arr.append(count)


for i in arr:
  print(i,end="")