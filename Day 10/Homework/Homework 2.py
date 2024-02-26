# For + Range მაგალითები:
#1)
for i in range(10):
    print("lol")

print("--------------------------------")

#2)
for i in range(10):
    print(i)

print("--------------------------------")

#3)
for i in range(int(2.0)):
    print(i)

print("--------------------------------")

#4)
for i in range(10 + 1):
    print(2)

print("--------------------------------")

#5)
for i in range(int(20.2) + 2):
    print(i)

print("--------------------------------")

#6)
for i in range(True):
    print(10)

print("--------------------------------")

#7
for i in range(True):
    print(i)

print("--------------------------------")

#8)
for i in range(False): #აქ არაფერი გამოიტანა რადგან ეს წინადადება არ არის მართალი
    print(10)

print("--------------------------------")

#9)
for i in range(20):
    print(type(2.0))

print("--------------------------------")

#10)
for i in range(12):
    print(type("luka"))

print("--------------------------------")

# if else მაგალითები:


#1)
number = int(input("Enter Your Age "))

if number > 20:
    print("Not Allowed")
else:
    print("Welcome!")

print("--------------------------------")


#2)
password = 1144

user_input = int(input("Enter Password!"))

if user_input != password:
    print("Password Incorrect!")
else:
    print("Succes!")

print("--------------------------------")


#3)
num = 10

if num > 0:
    print("This number is greater then 0!")
elif num < 0:
    print("this number is not greater then 0!")
else:
    print("this  number is 10")

print("--------------------------------")


#4)
    
number = 14

if num % 2==0:
    print("this number is even")
else:
    print("this number is odd")

print("--------------------------------")


#5)

text = "Luka akofiani"

if text:
    print("This String Is Not Empty")
else:
    print("This String Is Empty")

print("--------------------------------")

#6)

user_role = "CEO"

if user_role == "CEO":
    print("User Is CEO of this company")
else:
    print("User Is Not CEO of this company")

print("--------------------------------")


#7)

text = "LUKA AKOFIANI"

if text:
    print("String is not empty its filled")
else:
    print("String is empty its filled")

print("--------------------------------")

#8)
age = 17

if age > 18:
    print("You Cant Vote!")
else:
    print("you can vote")

print("--------------------------------")


#9)

Score = 90

if Score < 100:
    print("FAILED")
else:
    print("Well Done!")

print("--------------------------------")

#10)

kid_age = 10

if kid_age <= 20:
    print("You are not allowed to buy this!")
else:
    print("You are allowed to buy this!")

# მაგალითები while ფუნქციის:
    
#1)
    
number = 20

while number < 31:
    print("Playboy")
    number = number + 1

print("--------------------------------")


#2)
    
queue = 10

while queue < 11:
    print("wait")
    queue += 1
else:
    ("Go!")

print("--------------------------------")


#3)

countdown = 10
while countdown >= 1:
    print(countdown)
    countdown -= 1

print("--------------------------------")


#4)
    
message = "KAWASAKI"
repeat = 1

while repeat < 11:
    print(message)
    repeat = repeat + 1

print("--------------------------------")


#5)
    
password = ""

while password != "Code":
    password = input("Enter Your Password: ")
    if password != "Code":
        print("Try Again")
    else:
        print("Acces Granted!")

print("--------------------------------")

#6)
        
user_input = ""

while user_input != "Stop":
    user_input = input("Enter 'Stop' to end the question loop: ")

print("--------------------------------")

#7)
    
answer = ""

while answer != "Yes":
    answer = input("Are you 18 years old?: ")

    if answer == "Yes":
        print("You are Eligible!")
    else:
        print("Try again")










    
 

