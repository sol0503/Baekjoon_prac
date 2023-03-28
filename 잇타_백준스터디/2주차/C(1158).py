import sys
from collections import deque
n,k=map(int,(sys.stdin.readline().split()))
arr=[]
list=deque(range(1,n+1))

while list:
  for _ in range(k-1):
    list.append(list.popleft())
  arr.append(list.popleft())

print(str(arr).replace('[','<').replace(']','>'))

#추가적 공부 필요