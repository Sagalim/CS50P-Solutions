def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$", " ")) # one could also store it in a variable first


def percent_to_float(p):
    return float(p.replace("%", " ")) / 100 # same here, one could also store it in a variable first


main()