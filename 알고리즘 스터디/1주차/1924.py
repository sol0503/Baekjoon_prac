a,b=map(int,input().split())

date={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

day=0


for i in range(1,a):
  day+=date[i]

day+=b

day=day%7

arr=["SUN","MON","TUE","WED","THU","FRI","SAT"]

print(arr[day])
