#Q5WAP to calculate selling price of book based on cost price and discount

#Discount Amount = (Cost Price × Discount %) / 100
#Selling Price = Cost Price - Discount Amount

cost_price = float(input("Enter Cost Price: "))
discount = float(input("Enter Discount Percentage: "))

discount_amount = (cost_price * discount) / 100

selling_price = cost_price - discount_amount

print("Discount Amount =", discount_amount)
print("Selling Price =", selling_price)