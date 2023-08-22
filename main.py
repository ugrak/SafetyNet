menu = """0. Exit
1. Addition
2. Subtraction
3. Make Upper case
4. Make Lower case
"""


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

