menu = """0. Exit
1. Addition
2. Subtraction
3. Make Upper case
4. Make Lower case
"""


def get_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2

    except ValueError:
        return None, None



def get_letters():
    try:
        input_string = input("Enter a string: ")

        if not input_string.isalpha():
            raise ValueError("Input should only contain letters!")

        return input_string

    except ValueError:
        return


def main():
    option = str()
    while option != "0":
        print(menu)
        option = input("Enter an option: ")
        if option == "0":
            print("Bye")
        elif option == "1":
            print("Addition selected", end="\n\n")
        elif option == "2":
            print("Subtraction selected", end="\n\n")
        elif option == "3":
            print("Make Upper case selected", end="\n\n")
        elif option == "4":
            print("Make Lower case selected", end="\n\n")
        else:
            print("Wrong input", end="\n\n")


if __name__ == "__main__":
    main()

