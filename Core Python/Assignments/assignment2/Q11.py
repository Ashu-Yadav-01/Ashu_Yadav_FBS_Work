#11. Write a program to accept an integer amount from user and tell minimum
#number of notes needed for representing that amount.

#Logic
#Use floor division (//) to find the number of notes.
#Use modulus (%) to find the remaining amount.
amount = int(input("Enter Amount: "))

note2000 = amount // 2000
amount = amount % 2000

note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200

note100 = amount // 100
amount = amount % 100

print("2000 Notes =", note2000)
print("500 Notes =", note500)
print("200 Notes =", note200)
print("100 Notes =", note100)
print("Remaining Amount =", amount)