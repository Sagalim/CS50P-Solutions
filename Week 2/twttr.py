user_input = input("Input: ")


vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
result = ""

for c in user_input:
    if c in vowels:
        continue
    else:
        result += c


print("Output: " + result)