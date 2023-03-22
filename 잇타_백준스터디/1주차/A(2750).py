import sys
num = int(sys.stdin.readline())
arr=[]
for i in range(0, num):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for i in arr:
  print(i)
