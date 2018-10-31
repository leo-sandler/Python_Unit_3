import time
import random
# Calling a function: Syntax: function_name(list_of_params), or function_name() with empty brackets with no params


def print_halloween():
    print("Happy Halloween!")


print_halloween()


def print_halloween_1(times):
    for x in range(times):
        print("Happy Halloween!")


print_halloween_1(3)


def print_halloween_2(inny, outer):
    for x in range(outer):
        for y in range(inny):
            print("Happy Halloween!")


print_halloween_2(3, 3)
# This will print 9, due to the multiplication of 3 and 3. Also, 4 other will be printed for a total of 13
# This is a nested for loop


def print_halloween_3(inne, outer):
    for x in range(outer):
        print("Test")
        for y in range(inne):
            print("Happy Halloween!")


print_halloween_3(3, 3)
# This will print 3 tests, and 9 happy halloweens


def print_halloween_4(innar):
    if innar > 7:
        return True
    elif innar == 7:
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

# Spooky Function Tasks 1
# Create a function that has no parameters. It will use time.sleep(x) and random to, at a random time print "BOO!"


def sleepy_func():
    print("wait...")
    time.sleep(random.randint(1, 5))
    print("BOO!")


sleepy_func()

# Spooky Functions Task 2
# Create a function that returns trick or treat randomly
inner = random.randint(1, 2)


def trick_or_treat(inner):
    print("Wait 2 seconds...")
    time.sleep(2)
    if inner == 1:
        return "Python chose:  Trick"
    elif inner == 2:
        return "Python chose:  Treat"


print(trick_or_treat(inner))

# Spooky Task 3:
# Create a function that has 1 parameter, a string, adds "Spooky" to the beginning of that string, and returns it.
user_str = str(input("Enter Your Name: "))


def spooky_ad(user_str):
    spook = "Spooky " + user_str
    return spook


print("HELLO " + spooky_ad(user_str).upper())
