import sys
def count():
  input=list(sys.stdin.readline())
  b=[]
  for i in range(0,len(input)-1):
    if input[i]!=input[i+1]:
      if input[i] in b:
        return 0
      else:
        b.append(input[i])
  return 1  

a= int(sys.stdin.readline())
num=0
for i in range(a):
  num+=count()
print(num)