# float function >> they represent real numbers and are written with a decimal point 
# dividing the integer and the fractional parts.

num_1 = float(input("Enter first number please"))

operator = input("Enter operator please")

num_2 = float(input("Enter second number please"))


if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "/":
    print(num_1 / num_2)
elif operator == "*":
    print(num_1 * num_2)
else:
    print("operator does not exist")







