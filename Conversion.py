#Binary to Decimal and OctaDecimal to HexaDecimal
def bin2Dec(val):
    return int(val, 2)

def oct2Hex(val):
    return int(val, 8)

def reset():
    while True:
        try:
            num1 = input("Enter a binary number : ")
            print(bin2Dec(num1))
        except ValueError:
            print("Invalid literal in input with base 2")

        try:
            num2 = input("Enter a octal number : ")
            print(oct2Hex(num2))
        except ValueError:
            print("Invalid literal in input with base 8")

        Again = input("Do you want to continue?(yes/no) :").lower()
        if Again != "yes":
            print(" Exiting program. Goodbye!")
            break

reset()
