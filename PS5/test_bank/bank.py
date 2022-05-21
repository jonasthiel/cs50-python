def main():
    user_input = input("Greeting: ")
    print(f"${value(user_input)}")


def value(greeting):
    converted_input = greeting.lower().lstrip()
    if "hello" == converted_input[:5]:
        return 0
    elif "h" == converted_input[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()