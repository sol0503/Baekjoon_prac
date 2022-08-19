# i=0
# a=[]
# while i<9:
#   a.append(int(input()))
#   i+=1
# i=0
# num=0
# max=a[0]
# for i in range(9):
#   if(max<=a[i]):
#     max=a[i]
#     num=i+1
# print(max)
# print(num)

num_list=[]
for i in range(9):
  num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list))+1)