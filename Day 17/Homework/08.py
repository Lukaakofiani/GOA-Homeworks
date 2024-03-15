# 1

def username(name):
  print("Hello", name)

username("Luka")

print("-----------------------------------------")

# 2

def number(x, y):
  return x + y


print(number(1, 2))

print("-----------------------------------------")

# 3

numbers = 10

for i in range(numbers):
  print(i)

print("-----------------------------------------")

# 4

num = 15

if num < 16:
  print("16 is greater then 15!")
elif num >= 15:
  print("This Number is greater then or equals 15!")
else:
  print("This number is 15")

print("-----------------------------------------")

# 5

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)

print("-----------------------------------------")

# 6

list = [1, 2, 3, 4, 5, ]
num2 = 6, 7, 8, 9, 10, 11

list.append(num2)
print(list)

print("-----------------------------------------")

# 7

user_input = int(input("Enter First Number to calculate! "))
user_input2 = int(input("Enter Second Number to calculate "))

result = user_input + user_input2

print(result)




