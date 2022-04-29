numerator = 0
denominator = 0
while True:
    user_input = input("Fraction: ")
    modified_input = user_input.split("/")

    if modified_input[0].isdigit() and modified_input[1].isdigit():
        numerator = int(modified_input[0])
        denominator = int(modified_input[1])
    try:
        division = numerator / denominator
        if division <= 1:
            break
    except ZeroDivisionError:
        pass

if division > 0.99:
    fuel_gauge = "F"
elif division < 0.01:
    fuel_gauge = "E"
else:
    fuel_gauge = str(int(division * 100)) + "%"

print (fuel_gauge)