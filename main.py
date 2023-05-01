# calculator.py
def bitwise_and(x, y):
    return (x & y)
def bitwise_or(x, y):
    return (x | y)
def bitwise_not(x):
    return (~ x)
def bitwise_xor(x, y):
    return (x ^ y)

def add(x,y):
    ans =x+y
    return ans

def input_for_two_nums():
    x = int(input("Please enter first number: "))
    y = int(input("Please enter second number: "))
    return x,y

def menu ():
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. XOR")


def main():
    menu()
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        x, y = input_for_two_nums()
        result = bitwise_and(x, y)
        print(result)
    elif choice == 2:
        x ,y =input_for_two_nums()
        result = bitwise_or(x, y)
        print(result)
    elif choice == 3:
        x = int(input("Please enter first number: "))
        result = bitwise_not(x)
        print(result)
    elif choice == 4:
        x ,y =input_for_two_nums()
        result = bitwise_xor(x, y)
        print(result)
    else:
        print("Invalid choice")
if __name__ == '__main__':
    main()