def manual_replace():
    lst = [10, 11, 10, 11]
    return [20 if x == 10 else x for x in lst]
  


print(manual_replace())