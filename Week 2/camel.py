def main():
    user_input = input("camelCase: ")
    print("snake_case: " + convert(user_input))

def convert(string):
    result = ""
    for c in string:
        if c.islower():
            result += c
        elif c.isupper():
            result += "_" + c.lower()
    return result

main()
