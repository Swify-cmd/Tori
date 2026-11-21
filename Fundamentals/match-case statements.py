# match-case (switch) statements


def months(month):

    match month:
        case 1: # similar to if statement
            print("January")
        case 2: # similar to elif statement
            print("February")
        case 3:
            print("March")
        case 4:
            print("April")
        case 5:
            print("May")
        case 6:
            print("June")
        case 7:
            print("July")
        case 8:
            print("August")
        case 9:
            print("September")
        case 10:
            print("October")
        case 11:
            print("November")
        case 12:
            print("December")
        case _: # similar to else statement
            print("This is an invalid month")

month = int(input("Enter a number of a month: "))
months(month)
