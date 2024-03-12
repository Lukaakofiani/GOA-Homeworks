num = int(input())
fct = 1
if num == 0:
  print("it's 0")
elif num == 1:
  print("it's 1")
for i in range (1,num + 1):
  fct = fct * i
  print(fct)