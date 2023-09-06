n=int(input())

arr=[]
for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)

arr.sort()
minFir=arr[0][0]
minLast=arr[0][1]
min=minLast-minFir
count=0

for i in range(1,len(arr)):
    fir,last=arr[i][0],arr[i][1]
    len=last-fir
    if fir>=minLast:
        count+=1
        # print(fir,last)
        mainFir=fir
        minLast=last
    else:
        if last<minLast:
            mainFir=fir
            minLast=last



count+=1 #마지막꺼들어오기
print(count)


# 1. sort정렬후 젤 작은거를 min으로 기준잡고 앞자리, 뒷자리,뺀값을 각각설정 
# 2. 첫번째 if문은 fir을 기준으로 뒷숫자보다크면 회의1갠이미 들어간 이야기니까 count+1
# 3. 그렇지 않으면 겹치는 시간이 있는건데 그럴때는 뒷시간을 기준으로 더 작은걸선택해 다른 회의가 들어올수있게 해준다.
# 4. 마지막회의도 더해줘야하므로 +1