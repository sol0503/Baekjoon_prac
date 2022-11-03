import sys

word=list(map(str,sys.stdin.readline()))
alpa=[-1]*26
count=0
for i in word:
  ascii=ord(i)-97
  if ascii==-87:
    break
  if alpa[ascii]==-1:
    alpa[ascii]=count
    count+=1
  else:
    count+=1

  
for i in range(0,26):
  print(alpa[i],end=" ")