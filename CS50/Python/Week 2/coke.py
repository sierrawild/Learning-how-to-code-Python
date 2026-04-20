coins = [25, 10, 5]

inserted = 0

amount_due = 50

while inserted < 50:
    put_in = int(input('Insert Coin:').strip())

    if put_in in coins:
        inserted += put_in
        amount_due -= put_in

    if amount_due > 0:
        print(f"Amount Due: {amount_due}")

print(f"Change Owed: {abs(amount_due)}")
