user_input = input("Enter Your Name! ")

if user_input:
  last_character = user_input[-1]
  print("Last Characetr Of That Name Is: " + last_character)
else:
  print("Invalid input")