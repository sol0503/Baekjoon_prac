while True:
  try:
    a,b=map(int,input().split())
    print(a+b)
  except:
    break

  # 아무것도 없이 멈추고 싶을때는 에러나오는것을 이용하여 try,except문을 써주면 된다.