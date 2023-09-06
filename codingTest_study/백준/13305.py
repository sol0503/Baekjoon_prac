n=int(input())

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

min=arr2[0]
money=0
for i in range(0,len(arr1)):
    if i==0:
        money+=arr1[i]*arr2[i]
    else:
        if arr2[i]>=min:
            money+=min*arr1[i]

        else:
            min=arr2[i]
            money+=min*arr1[i]
print(money)