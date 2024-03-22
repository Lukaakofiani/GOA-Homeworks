def request_names_to_list():
    first_input = input("Enter Your User! ")
    second_input = input("EnterYour Lastname! ")

    names_list = first_input, second_input

    return names_list

add_names = request_names_to_list()
print(add_names)