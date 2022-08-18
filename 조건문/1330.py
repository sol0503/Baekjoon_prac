number=input().split()
A,B=list(map(int,number))
if A>B:
  print(">")
elif A==B:
  print("==")
else:
  print("<")