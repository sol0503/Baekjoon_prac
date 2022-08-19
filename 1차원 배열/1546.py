num=int(input())
a=list(map(int,input().split()))
a_list=[]
a_max=max(a)
for i in  a:
  a_list.append(i/a_max*100)
s=sum(a_list)
avg=s/num
print(avg)