import sys

arr={"c=","c-","lj","nj","s=","z=","d-"}
a=list(sys.stdin.readline())
count=0
i=0
while(i<len(a)-1):
  if a[i]=="d":
    if i+2<=len(a)-1:
      str=a[i]+a[i+1]+a[i+2]
      if str=="dz=":
        count+=1
        i+=2
      else:
        if i+1<=len(a)-1:
          str=a[i]+a[i+1]
          if str=="d-":
            count+=1
            i+=1
          else:
            count+=1
    else:
      if i+1<=len(a)-1:
        if str=="d-":
          count+=1
          i+=1
        else:
          count+=1
      else:
        count+=1
  else:
    if i+1<len(a)-1:
      str=a[i]+a[i+1]
      if str in arr:
        count+=1
        i+=1
      else:
        count+=1
    else:
      count+=1
  i+=1
print(count)