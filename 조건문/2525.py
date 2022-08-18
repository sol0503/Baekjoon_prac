A,B=map(int,input().split())
C=int(input())
if B+C>=60:
  x=(B+C)%60
  y=(B+C)//60
  if y+A>=24:
    A=(A+y)-24
  else:
    A=A+y
  B=x
else:
  B=B+C
print(A,B)

