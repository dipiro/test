while True:
    print("For addition write 'plus'")
    print("For subtraction write minus")
    print("for an exit enter exit")
    user_input = input("Enter: ")

    if user_input == "exit":
        break
    elif user_input == "plus":
        x = float(input("Number: "))
        y = float(input("Number: "))
        sum = str(x + y)
        print("Result: " + sum)
    elif user_input == "minus":
        x = float(input("Number:"))
        y = float(input("Number:"))
        sum = str(x - y)
        print("Result: " + sum)
    else:
        print("Error")