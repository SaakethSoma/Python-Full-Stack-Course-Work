name=input("enter the name:")
mobileno= int(input("enter the mobileno :"))
product_1=input("enter the product-1:")
price_1= float(input("enter the product-1 price:"))
product_2=input("enter the product-2:")
price_2= float(input("enter the product-2 price:"))
product_3=input("enter the product-3:")
price_3= float(input("enter the product-3 price:"))

print(f"{name}your Bill")
print(f"{product_1}: $ {price_1}")
print(f"{product_2}: $ {price_2}")
print(f"{product_3}: $ {price_3}")

total_bill= price_1 + price_2 + price_3
print(f"{total_bill:} your total bill is:")
