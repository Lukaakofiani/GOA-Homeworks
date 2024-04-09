user_input = int(input("Enter Your Number: "))


def numbers(num):
  lst = []
  for i in range(len(num) -1, -1, user_input):
    if num[i] % 4 == 0:
      lst.append(i)
  return lst


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

oll = numbers(lst)
print(lst)