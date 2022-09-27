from array import array


arr=(input()).upper()
sum=0
for a in arr:
  if a=='A' or a=='B' or a=='C':
    sum+=3
  elif a=='D' or a=='E' or a=='F':
    sum+=4
  elif a=='G' or a=='H' or a=='I':
    sum+=5
  elif a=='J' or a=='K' or a=='L':
    sum+=6
  elif a=='M' or a=='N' or a=='O':
    sum+=7
  elif a=='P' or a=='Q' or a=='R' or a=='S':
    sum+=8
  elif a=='T' or a=='U' or a=='V':
    sum+=9
  elif a=='W' or a=='X' or a=='Y' or a=='Z':
    sum+=10
  else:
    sum+=0

print(sum)