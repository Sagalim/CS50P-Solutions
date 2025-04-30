# storing user's mathematical expression
user_input = input("Expression: ")

# storing the components of the expression
x, y, z = user_input.split(" ")

x = float(x)
z = float(z)

if y == "+":
    result = x + z
    print(result)
elif y == "-":
    result = x - z
    print(result)
elif y == "*":
    result = x * z
    print(result)
elif y == "/":
    result = x / z
    print(result)
