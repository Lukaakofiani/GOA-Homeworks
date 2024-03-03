num1 = int(input("Enter Number! "))
num2 = int(input("Enter Second Number! "))
sum = 0

for num in range(num1, num2 +1):
  sum = sum + num
  print(num)
print(sum)