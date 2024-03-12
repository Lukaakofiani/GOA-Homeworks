count = 0

password = "Goa best"


while True != password:
  user_input = input("Enter Password! ")
  if user_input == password:
    print("You have entered correct password!")
    break
  else:
    print("try again")
    count+=1
    print(count)
    