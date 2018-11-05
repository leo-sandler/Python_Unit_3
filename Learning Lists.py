colours = ['red', 'blue', 'green']
print(colours[0])  # This prints red
print(colours[2])  # This prints green
print(len(colours))  # This prints the total amnt of things in the list
colours1 = ['orange', 'yellow', 'purple']
b = colours+colours1
b.sort()  # Sort before using in a loop
for x in b:
    print(x)
    # This prints it on multiple lines
