import random


def area_of_triangle(base, height):
    area = (base * height) / 2
    return area


triangle_area = area_of_triangle(4, 3)
print(triangle_area)


# Above is the first part of the lesson

# Task 1
def printer():
    print("Hello World")


printer()


# Task 2
def printerx5():
    five_time_input = input("Please enter something: ")
    for x in range(0, 5):
        print(five_time_input)


printerx5()


# Task 3
def uppercase():
    uppercase_input = input(str("Input something lower-cased: ")).upper()
    print(uppercase_input)


uppercase()


# Task 4
def check(num_1, num_2, num_3, rand_1, rand_2, rand_3):
    if (rand_1 == num_1 or rand_1 == num_2 or rand_1 == num_3) and (rand_2 == num_1 or rand_2 == num_2 or
            rand_2 == num_3) and (rand_3 == num_1 or rand_3 == num_2 or rand_3 == num_3):
        print("The numbers match")
    else:
        print("No match")


def lottery():
    num_1 = int(input("Please enter a number between 1 and 5: "))
    num_2 = int(input("Please enter a number between 1 and 5: "))
    num_3 = int(input("Please enter a number between 1 and 5: "))
    rand_1 = random.randint(1, 5)
    print(str(rand_1) + " Is the 1st random number")
    rand_2 = random.randint(1, 5)
    print(str(rand_2) + " Is the 2nd random number")
    rand_3 = random.randint(1, 5)
    print(str(rand_3) + " Is the 3rd random number")
    check(num_1, num_2, num_3, rand_1, rand_2, rand_3)


lottery()

print("Trying a new commit")


