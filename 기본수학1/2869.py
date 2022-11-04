import sys
A,B,V=map(int,sys.stdin.readline().split())
day=(V-B)/(A-B)
if day!=int(day):
  day=int(day)+1

print(int(day))