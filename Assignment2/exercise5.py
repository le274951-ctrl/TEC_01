diameter1 = float(input("Enter the diameter of pizza 1 in cm: "))
price1 = float(input("Enter the price of pizza 1 in USD: "))

diameter2 = float(input("Enter the diameter of pizza 2 in cm: "))
price2 = float(input("Enter the price of pizza 2 in USD: "))
def unit_price(diameter, price):
    diameter_meter = diameter / 100
    radius = diameter_meter / 2
    area = 3.14159 * radius ** 2
    return price / area

unit_price1 = unit_price(diameter1, price1)
unit_price2 = unit_price(diameter2, price2)

if unit_price1 < unit_price2:
    print("Pizza 1 provides better value for money.")
elif unit_price2 < unit_price1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")