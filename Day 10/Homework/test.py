answer = ""
while answer != "Yes":
    answer = input("Are you 18 years old?: ")
    if answer == "Yes":
        print("You are Eligible!")
    else:
        print("Try again")