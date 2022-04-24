def convert(phrase):
    if ":)" and ":(" in phrase:
        converted_phrase = phrase.replace(":)", "🙂").replace(":(", "🙁")
        print(converted_phrase)
    elif ":)" in phrase:
        converted_phrase = phrase.replace(":)", "🙂")
        print(converted_phrase)
    elif ":(" in phrase:
        converted_phrase = phrase.replace(":(", "🙁")
        print(converted_phrase)
    else:
        print(phrase)

def main():
    user_input = input()
    convert(user_input)

main()