arr=list(input().upper())
arr_sort=sorted(arr)
arr_set=list(dict.fromkeys(arr_sort))
b=[]
count=1
a=0

if len(arr_sort)==1:
  b.insert(a,count)
else:
  for i in range(0,len(arr)-1):
    if arr_sort[i]==arr_sort[i+1]:
      if i+2>len(arr):
        count+=1
        b.insert(a,count)
      else:
        count+=1
    else:
      b.insert(a,count)
      a+=1
      count=1
  b.insert(a,count)
max=-1
if len(arr_sort)==1:
  print(arr_set[0])
else:
  count=0
  m=-1
  for i in range(0,len(b)):
    if max<b[i]:
      max=b[i]
      count=0
      m=i
    elif max==b[i]:
      count+=1
  if count!=0:
    print("?")
  else:
    print(arr_set[m])