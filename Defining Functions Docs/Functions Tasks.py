# Task 1


def product_function():
    num_1 = int(input("Enter the first #: "))
    num_2 = int(input("Enter the second  #: "))
    prod = (num_1*num_2)

    return prod


print(product_function())

# Task 2


def comp_nums():
    num_1 = int(input("Enter the first #: "))
    num_2 = int(input("Enter the second  #: "))
    comp_checking(num_1, num_2)


def comp_checking(num_1, num_2):
    if num_1 == num_2:
        print("True")
    else:
        print("False")


print(comp_nums())
# Not sure why this states none after running, but it works properly.

# Task 3


def main():
    import math

    def quick_pythag():
        side_1_input = int(input("Please enter the first triangle side length: "))
        side_2_input = int(input("Please enter the second side triangle length: "))
        print("Side 1 squared plus side 2 squared will equal the hypotenuse squared")
        s1_squared: int = side_1_input * side_1_input
        s2_squared: int = side_2_input * side_2_input
        print(str(s1_squared) + " is side 1 squared")
        print(str(s2_squared) + " is side 2 squared")
        final_ans_o = math.sqrt(s1_squared + s2_squared)
        output_0 = round(final_ans_o, 2)
        print(str(output_0) + " is the length of the hypotenuse")

    def tip_calc():
        bill_amnt = int(input("Please enter the bill amount: $"))
        tip_amnt = int(input("Please enter the tip amount in percent"
                             ", For example, '20': %"))
        final_ans_c = (bill_amnt * tip_amnt / 100)
        output_1 = round(final_ans_c, 2)
        print("$" + str(output_1) + " is the final tip amount")

    def temp_converter():
        cel_or_fa = input("Please choose between a final answer of Celsius or Fahrenheit: ")
        if cel_or_fa == "C" or cel_or_fa == "c" or cel_or_fa == "Celsius" or cel_or_fa == "celsius":
            fa_input = int(input("Please enter the temperature in Fahrenheit: "))
            fa_to_cel = (fa_input - 32) * 5 / 9
            print(str(fa_input) + "° Fahrenheit is " + str(fa_to_cel) + "° Celsius")
        elif cel_or_fa == "f" or cel_or_fa == "F" or cel_or_fa == "Fahrenheit" or cel_or_fa == "fahrenheit":
            cel_input = int(input("Please enter the temperature in Celsius: "))
            cel_to_fa = (cel_input * 9 / 5 + 32)
            print(str(cel_input) + "° Celsius is " + str(cel_to_fa) + "° + Fahrenheit")

    print("Please enter 'Q' for Quick Pythagoras, "
          "enter 'C' for Tip Calculator, "
          "enter 'T' for Temperature Converter"
          ", or enter 'S' to end the program")
    menu_input: str = str(input("Enter one of these options: "))
    if menu_input == "Q" or menu_input == "q":
        quick_pythag()
    elif menu_input == "c" or menu_input == "C":
        tip_calc()
    elif menu_input == "t" or menu_input == "T":
        temp_converter()
    elif menu_input == "S" or menu_input == "s":
        exit()
    else:
        print("Please enter a valid option")
        main()
    restart = input("Do you want to start again? ").lower()
    if restart == "Y" or restart == "y" or restart == "Yes" or restart == "yes":
        main()
    else:
        exit()


main()

# Task 4
