#Diego Osornio
#11/19/2024

#Functions
#Add Num1 with num2 and print the result
while True:
        def add(num1, num2):
            result = num1 + num2 #One possible Solution
            print(result)

        def subtract(num1, num2):
            result = num1 - num2
            print(result)

        def Multiply(num1, num2):
            result = num1 * num2
            print(result)

        def divide(num1, num2):
            result = num1 / num2
            print(result)

        def Calc():
            print("Welcome to the Simple Calculator")
        print("Select an Operation")
        print("""1.Addition
    2.Subtraction
    3.Muliplication
    4.Division
    5.Quit""")
        option= int(input("(1-5)Select Option: "))
        if option == 1:
            int1 = int(input("Enter First Number: "))
            int2 = int(input("Enter Second Number: "))
            add(int1, int2)
        if option == 2:
            int3 = int(input("Enter First Number: "))
            int4 = int(input("Enter Second Number: "))
            subtract(int3, int4)

        if option == 3:
            int5 = int(input("Enter First Number: "))
            int6 = int(input("Enter Second Number: "))
            Multiply(int5, int6)

        if option == 4:
            int7 = int(input("Enter First Number: "))
            int8 = int(input("Enter Second Number: "))
            divide(int7, int8)

        if option == 5:
            print("GoodBye")
            break


#main
calc()
