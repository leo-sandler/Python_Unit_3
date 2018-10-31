# Calling a function: Syntax: function_name(list_of_params), or function_name() with empty brackets with no params
def print_halloween():
    print("Happy Halloween!")


print_halloween()


def print_halloween_1(times):
    for x in range(times):
        print("Happy Halloween!")


print_halloween_1(3)


def print_halloween_2(inner, outer):
    for x in range(outer):
        for y in range(inner):
            print("Happy Halloween!")


print_halloween_2(3, 3)
# This will print 9, due to the multiplication of 3 and 3. Also, 4 other will be printed for a total of 13
# This is a nested for loop


def print_halloween_3(inner, outer):
    for x in range(outer):
        print("Test")
        for y in range(inner):
            print("Happy Halloween!")


print_halloween_3(3, 3)
# This will print 3 tests, and 9 happy halloweens


def print_halloween_4(inner):
    if inner > 7:
        return True
    elif inner == 7:
        return False
    else:
        return "Boo"


user_num = int(input("Gimme a Number: "))
# User num should be outside the defined function if you want to use it later, but can be used within the function if
# it is not used again

print(print_halloween_4(user_num))
# W/o brackets this will not print anything. Therefore, with the print on the outside the return values will print.

print(print_halloween_4(int(input("Gimme a Number: "))))
# This notation does the exact same thing
