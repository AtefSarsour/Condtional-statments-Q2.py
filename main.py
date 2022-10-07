first_input = input("Enter your first number")
second_input = input("Enter your second number")
if first_input.isdigit():
    pass
else:
    print("Please enter a valid number")
    exit()
if second_input.isdigit():
    pass
else:
    print("please enter a valid number")
    exit()
print("app options")
print("1.+\n2.-\n3.x\n4./")
user_input = input("Please choose your operation")
if user_input == ("+") or user_input == ("1"):
    result =(int(first_input) + int(second_input))
    print(result)
if user_input == ("-") or user_input == ("2"):
    result =(int(first_input)- int(second_input))
    print(result)
if user_input == ("x") or user_input == ("3"):
    result =(int(first_input) * int(second_input))
    print(result)
if user_input == ("/") or user_input == ("4"):
    result = (int(first_input) / int(second_input))
    print (result)
second_operation= input("Do you want to make more operations on result?\n1.Round number\n2.Not decimal number")
if second_operation == ("1") or second_operation == ("Round number"):
    print (round(result))
elif second_operation == ("2") or second_operation == ("Not decimal number"):
    print(int(result))