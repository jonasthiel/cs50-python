input = input("camelCase: ")
snake_case = ""
for letter in input:
    if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        snake_case += "_" + letter.lower()
    else:
        snake_case += letter
print("snake_case:", snake_case)