import math

def radians_to_degrees():
    radians = int(input("Enter a value in radians: "))
    print("Radians: " + str(radians))
    degrees = (radians / math.pi) * 180
    new_degrees = round(degrees, 2)
    print("Degrees: " + str(new_degrees))


radians_to_degrees()
