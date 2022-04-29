months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

end = False
while not end:
    user_input = input("Date: ")
    try:
        month, day, year = user_input.split("/")
        if (int(year) >= 0) and (12 >= int(month) >= 1) and (31 >= int(day) >= 1):
            print(f'{year}-{month.rjust(2, "0")}-{day.rjust(2, "0")}')
            break
    except:
        pass
    try:
        month, day, year = user_input.replace(",", "").split(" ")
        if (month in months) and (int(year) >= 0) and (31 >= int(day) >= 1):
            print(f'{year}-{str(months.index(month) + 1).rjust(2, "0")}-{day.rjust(2, "0")}')
            break
    except:
        pass