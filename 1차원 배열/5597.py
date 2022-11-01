arr=[]
for i in range(1,29):
  a=int(input())
  arr.insert(i,a)

arr=sorted(arr)
k=0
for i in range(1,31):
  if i not in arr:
    print(i)
    k+=1
  if k==2:
    break

  




