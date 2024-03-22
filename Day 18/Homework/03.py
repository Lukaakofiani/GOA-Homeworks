def nums():
  lst = []

  ll = []

  mm = []
  num1 = int(input("enter num1: "))
  num2 = int(input("enter num2: "))
  for i in range(num1 , num2+1):
    lst.append(i)
    if i % 2 == 0:
      m = i ** 2
      ll.append(m)
    else: 
      k = i ** 2
      mm.append(k)
  print(ll)
  print(mm)
    

nums()
    


  

