#a program to calculate the circumference of a circle
def circumference(diameter):
    pi = 3.142
    return pi * diameter
d = int(input("Enter the diameter of the circle: "))
print("The circumference of the circle is:", circumference(d))