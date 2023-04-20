import sys
arr=list(map(int,sys.stdin.readline().split()))

ex=[1,2,3,4,5,6,7,8,9]

if arr[0]==1:  
  for i in range(8):
      if arr[i]==ex[i]:
          continue
      else:
          print("mixed")
          break
  if i==7: 
    print("ascending")
elif arr[0]==8:
  for i in range(8):
      if arr[-i-1]==ex[i]:
          continue
      else:
          print("mixed")
          break
  if i==7: 
    print("descending")
else:
    print("mixed")
      
