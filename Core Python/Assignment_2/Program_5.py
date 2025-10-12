#WAP to calculate selling price of book based on cost price and discount.

cost_price = float(input("Enter cost price :"))
discount_price = float(input("Enter discount price :"))

discount_amount = (cost_price * (discount_price / 100))
selling_price = cost_price - discount_price

print(f"cost price = {cost_price}")
print(f"dicount price = {discount_price}")
print(f"selling price = {selling_price}")