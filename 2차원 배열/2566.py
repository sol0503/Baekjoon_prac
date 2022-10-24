import sys


x=0
y=0
max=-1
for n in range(1,10):
    num=sys.stdin.readline().split()
    for i in range(1,10):
      if max<int(num[i-1]):
        max=int(num[i-1])
        x=n
        y=i

print(max)
print(x,y)


