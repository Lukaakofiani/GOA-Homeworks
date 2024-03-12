user_input = int(input("Enter Your Number "))
even_numbers_list = []

for i in range(user_input + 1):
  if i % 2 == 0:
    even_numbers_list.append(i)

print(even_numbers_list)
  

