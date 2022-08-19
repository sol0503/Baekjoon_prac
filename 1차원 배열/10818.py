num=int(input())
a=list(map(int,input().split()))
# min=a[0]
# max=a[0]
# for i in range(num):
#   if(min>=a[i]):
#     min=a[i]
#   if(max<=a[i]):
#     max=a[i]
# print(min,max)

print(min(a),max(a))