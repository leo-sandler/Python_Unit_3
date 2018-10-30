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
