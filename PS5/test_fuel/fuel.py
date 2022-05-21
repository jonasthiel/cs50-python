def main():
    user_input = input("Fraction: ")
    division = convert(user_input)
    fuel_gauge = gauge(division)
    print(fuel_gauge)


def convert(fraction):
    modified_input = fraction.split("/")
    if modified_input[0].isdigit() and modified_input[1].isdigit():
        if int(modified_input[1]) == 0:
            raise ZeroDivisionError
        else:
            if (0 <= int(modified_input[0]) <= 100) and (0 <= int(modified_input[1]) <= 100):
                if int(modified_input[0]) > int(modified_input[1]):
                    raise ValueError
                else:
                    division = int(int(modified_input[0]) / int(modified_input[1]) * 100)
                    return division
            else:
                raise ValueError
    else:
        raise ValueError


def gauge(percentage):
    if percentage >= 99:
        fuel_gauge = "F"
    elif percentage <= 1:
        fuel_gauge = "E"
    else:
        fuel_gauge = str(percentage) + "%"
    return fuel_gauge


if __name__ == "__main__":
    main()