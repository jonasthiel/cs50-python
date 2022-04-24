input = input("Input: ")
output = ""
for letter in input:
    if letter.lower() not in ["a", "e", "i", "o", "u"]:
        output += letter
print("Output:", output)