'''Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.'''

total = 0

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    amount = float(input(f"Enter ticket amount for person {i}: "))

    if age < 12:
        amount = amount - (amount * 0.30)
    elif age > 59:
        amount = amount - (amount * 0.50)

    total += amount

print("Total Ticket Amount =", total)