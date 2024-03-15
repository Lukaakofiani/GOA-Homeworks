def strings(names):
  lst = []
  for letters in names:
    if len(letters) > 5:
      lst.append(letters)
  return lst

list = ["Luka", "Giorgi", "Salome", "Deme"]
other_list = strings(list)

print(other_list)
