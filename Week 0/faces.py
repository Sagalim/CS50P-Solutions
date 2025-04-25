# input from the user
user_input = input("Your input: ")

# convert emoticons to actual emoji
print(user_input.replace(":)", "🙂").replace(":(", "🙁"))
