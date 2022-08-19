remain_list=[]
for i in range(10):
  a=int(input())
  b=a%42
  remain_list.append(b)
s=set(remain_list)

print(len(s))

# set함수는 중복을 제거하기 위한 필터역할을 해준다.