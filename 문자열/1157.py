arr=list(input().upper())
arr_sort=sorted(arr)
arr_set=list(set(arr_sort))
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
max=0
m=0
counting=0
if len(arr_sort)==1:
  print(arr_set[0])
else:
  for i in range(0,len(b)):
    if counting<b[i]:
      max=i
      counting=b[i]
    if counting==b[i]:
      m=counting
  if m==counting:
    print("?")
  else:
    print(arr_set[max])
print(arr_sort)
print(arr_set)
print(b)

고치기