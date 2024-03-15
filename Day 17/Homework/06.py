def string_length(string_list):
  lst = []
  for strings in string_list:
    lst.append(len(strings))
  return (lst)

inputs = ["Luca", "Gio", "Filk", "Porsche"]
other_list = string_length(inputs)
print(other_list)