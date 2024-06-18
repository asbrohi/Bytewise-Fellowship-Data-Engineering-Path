#this assignment is all about if else statement and also fucntions

hours_in_day = 24
unit_of_conversion = "hours"
def book_reservation(no_of_days):
    if no_of_days > 0:
        return f"{no_of_days} days will be equal to {no_of_days * hours_in_day} {unit_of_conversion}"
    elif no_of_days == 0:
        return "You have entered 0 digit"
    else:
        return "You have entered negative no of days"


def to_check_input():
    if day.isdigit():
        no_of_days = int(day)
        print(book_reservation(no_of_days))
    else:
        print("Your input is not number!")

day = input("Enter the number of days you want to convert: ")

to_check_input()






