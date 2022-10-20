import sys
def bee(a):
  count=1
  num=0
  sum=1
  while sum<a:
    count+=1
    num+=6
    sum+=num
  return count
a=int(sys.stdin.readline())
print(bee(a))

