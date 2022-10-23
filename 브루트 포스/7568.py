import sys

member=int(sys.stdin.readline())
kg=[]
cm=[]

for i in range(0,member):
  a=sys.stdin.readline().split()
  kg.append(int(a[0]))
  cm.append(int(a[1]))

result=[]

for i in range(0,member):
  count=0
  for k in range(0,member):
    if kg[i]<kg[k]:
      if cm[i]<cm[k]:
        count+=1
  count+=1
  result.append(count)

for i in result:
  print(i,end=" ")
