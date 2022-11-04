import sys
num=int(sys.stdin.readline())

line=0
end=0

while True:
  line+=1
  end+=line
  if num<=end:
    break

count=end-num

if line%2==0:
  print(str(line-count)+"/"+str(count+1))
else:
  print(str(count+1)+"/"+str(line-count))