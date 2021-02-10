# write a program to calculate area of box 

# Declare Variable and accept user input

l = float(input("Enter Length of a box (in cm) => "))
w = float(input("Enter Width of a box (in cm) => "))
h = float(input("Enter Height of a box (in cm) => "))

# Calculating area (a)\

a = 2*((l*w)+(l*h)+(w*h))

# Print processed output

print("Area of box (in square cm) is",a)
