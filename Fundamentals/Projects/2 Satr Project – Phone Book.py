number_holder = {
    'Amal': '1111111111',
    'Mohammed': '2222222222',
    'Khadijah': '3333333333',
    'Abdullah': '4444444444',
    'Rawan': '5555555555',
    'Faisal': '6666666666',
    'Layla': '7777777777'
}

name_or_number = input("Enter the name or the number: ")


if name_or_number.isdigit():
    for name, number in number_holder.items():
        if number == name_or_number:  
            print(f"The name belonging to the number {name_or_number} is {name}.")
            break  
    else:
        print(f"Sorry, the number {name_or_number} is not found in the phone book.")
else:
    if name_or_number in number_holder:
        print(f"The phone number is: {number_holder[name_or_number]}")
    else:
        print(f"Sorry, the name {name_or_number} is not found in the phone book.")
