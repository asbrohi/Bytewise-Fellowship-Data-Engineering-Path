#this assignment is all about if else statemnt

def book_reservation(category, day):
    if day == "Monday" and category == "Premium":
        print("You can book the reservation")
    elif day == "Tuesday" and category == "Medium":
        print("You can book the reservation")
    else:
        print("Sorry the reservations are not availble")


day = input("Enter the name of day and category you want a reservation: ")
category = input("Enter the category you want to reserve: ")
book_reservation(category, day)