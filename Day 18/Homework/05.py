def word_input():
  first_input = input("Enter Word! ")

  reversed_input = first_input[::-1]

  return reversed_input


new_list = word_input()
print(new_list)
