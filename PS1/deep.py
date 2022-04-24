input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
converted_input = input.lower().replace(" ", "").replace("-", "")
if "42" == converted_input:
    print("Yes")
elif "fortytwo" == converted_input:
    print("Yes")
else:
    print("No")