def main():
    user_input = input("What time is it? ")
    converted_input = convert(user_input)
    if 7 <= converted_input <= 8:
        print("breakfast time")
    elif 12 <= converted_input <= 13:
        print("lunch time")
    elif 18 <= converted_input <= 19:
        print("dinner time")

def convert(time):
    if len(time) == 4:
        converted_input = float(time[0]) + float(time[2] + time[3]) / 60
    else:
        converted_input = float(time[0] + time[1]) + float(time[3] + time[4]) / 60
    return converted_input

if __name__ == "__main__":
    main()