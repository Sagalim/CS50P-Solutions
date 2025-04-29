# asking user to greet
user_input = input("Greeting: ").lower().lstrip(" ")

# if the greeting starts with 'hello'
if user_input.startswith("hello"):
    print("$0")
# if the greeting starts with the letter 'h'
elif user_input.startswith("h"):
    print("$20")
else:
    print("$100")
