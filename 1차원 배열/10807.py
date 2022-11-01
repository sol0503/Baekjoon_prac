import sys

a=int(sys.stdin.readline())

arr=list(map(int,sys.stdin.readline().split()))
n=int(sys.stdin.readline())
count=0
for i in range(a):
  if arr[i]==n:
    count+=1

print(count)