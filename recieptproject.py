lovely_loveseat_description = """ 
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
print(lovely_loveseat_description)
lovely_loveseat_price = 254.00
print("The price retails" + " " + str(lovely_loveseat_price))
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wife x 28 inches deep. Black.
"""
print(stylish_settee_description)

stylish_settee_price = str(180.50)
print("The price retails" + " " + stylish_settee_price)

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade
"""
print(luxurious_lamp_description)
luxurious_lamp_price = 52.15
print("The price reails" + " " + str(luxurious_lamp_price))

sales_tax = 0.88

customer_one_total = lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization = lovely_loveseat_description + luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

print("Customer Ones Items:")
print(customer_one_itemization)
print("Customer Ones Total:")
print(customer_one_total)

