amount_due = 50
owed_change = 0
while amount_due > 0:
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in [5, 10, 25]:
        amount_due -= inserted_coin
    if amount_due <= 0:
        owed_change -= amount_due
        print("Change Owed:", owed_change)
    else:
        print("Amount Due:", amount_due)