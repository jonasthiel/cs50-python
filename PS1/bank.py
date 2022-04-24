input = input("Greeting: ")
converted_input = input.lower().lstrip()
if "hello" == converted_input[:5]:
    print("$0")
elif "h" == converted_input[0]:
    print("$20")
else:
    print("$100")