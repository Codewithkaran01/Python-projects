print("Thank you for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L \n").lower()
add_pepperoni = input("Do you want pepperoni? Y or N\n").lower()
extra_cheese = input("Do you want extra cheese? Y or N\n").lower()

bill = 0


if size not in ["s", "m", "l"]:
    print("Invalid size input")
elif add_pepperoni not in ["y", "n"]:
    print("Invalid pepperoni input")
elif extra_cheese not in ["y", "n"]:
    print("Invalid cheese input")
else:

    if size == "s":
        bill += 15
    elif size == "m":
        bill += 20
    elif size == "l":
        bill += 25


    if add_pepperoni == "y":
        if size == "s":
            bill += 2
        else:
            bill += 3


    if extra_cheese == "y":
        bill += 1

    print(f"Your total bill is ${bill}")