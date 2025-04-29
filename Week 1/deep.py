# getting user's input
user_input = input("Your answer: ")

# check the user's input using a match pattern
match user_input.lower().replace(" ", ""):
    case "42" | "forty-two" | "fortytwo":
        print("Yes")
    case _:
        print("No")
