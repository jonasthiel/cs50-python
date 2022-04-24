input = input("Expression: ")
modified_input = input.split()
if modified_input[1] == "+":
    print(float(modified_input[0]) + float(modified_input[2]))
elif modified_input[1] == "-":
    print(float(modified_input[0]) - float(modified_input[2]))
elif modified_input[1] == "*":
    print(float(modified_input[0]) * float(modified_input[2]))
elif modified_input[1] == "/":
    print(float(modified_input[0]) / float(modified_input[2]))