amount, paid = 50, 0
denominations = [25, 10, 5]

while paid < amount:
    print(f"Amount Due: {amount - paid}")
    user_input = int(input("Insert Coin: "))

    if user_input in denominations:
        paid += user_input
    else:
        print("Invalid coin.")

print(f"Change Owed: {paid - amount}")
