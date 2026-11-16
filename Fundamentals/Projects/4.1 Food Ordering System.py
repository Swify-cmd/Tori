# upgraded version of the little project
    
import time

menu = {
    'pizza': 22,
    'shawarma': 12,
    'burger': 15
}

while True:
    menu_search = input(f"What would you like to order?: ").strip().lower()

    if menu_search not in menu:
        print(f"{menu_search} is an invalid order... try again")
        continue

    print(f"Your order will be {menu_search} ${menu[menu_search]} ")
    confirmation = input("Type (Confirm) to confirm or (Back) to go back to the menu: ").strip().lower()

    if confirmation == "confirm":
        print("Your order will be delivered in 21 minutes!")
        break

    elif confirmation == "back":
        print("Going back to the menu...")
        continue
    
    else:
        print(f"{confirmation} is not a valid input")
