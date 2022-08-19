n=int(input())
for _ in range(n):
  a=list(map(int,input().split()))
  # sum=0
  # for i in range(1,a[0]+1):
  #   sum+=a[i]
  # avg=sum/a[0] 
  avg=sum(a[1:])/a[0]
  count=0
  for i in range(1,a[0]+1):
    if avg<a[i]:
      count+=1
  c=count/a[0]*100
  print(f'{c:.3f}%')